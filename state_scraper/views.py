from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from scraper import get_contents_of_urls

from state_scraper import models

"""
Basic functional views to handle login, logout, a simple home
page and a geodata page based on the actions of the user on
their home page.
"""


def login_user(request):
    """
    Very basic login view. If the user authenticates,
    they are taken to the home directory; else they
    are redirected to login again.

    :param request:
    :return:
    """
    # flush any previous login
    logout(request)

    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/home/')
    return render_to_response('registration/login.html', context_instance=RequestContext(request))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/login/')


@login_required(redirect_field_name=None)
def home(request):
    """
    Renders the home page for an authenticated user;
    Otherwise it returns them to the login.
    The home page will display hyperlinks for all the
    different state codes as well as a single link for
    all states, which will take them to the geodata view.
    The request.GET's 'state' parameter will be set to
    the corresponding state.

    :param request:
    :return:
    """
    return render_to_response('scraper/home.html', {'username': request.user.username, 'states': models.states})


@login_required(redirect_field_name=None)
def geodata(request):
    """
    Based on the 'state' parameter of the GET request,
    the user will be shown the geolocation data for all
    the counties in the selected state. If all states are
    selected or no valid state is selected, then the geolocation
    data will be displayed for all states.
    :param request:
    :return:
    """
    base_url = "http://api.sba.gov/geodata/city_county_links_for_state_of/"

    if request.GET:
        state = request.GET['state']

        # Simply return all the states in the case where the 'all states' link is clicked or if anyone monkeys with
        # the GET parameters.
        if state not in models.states:
            state_urls = [base_url + state + '.json' for state in models.states]
        else:
            # Create a list with a single item, as the get_contents_of_urls expects a list
            state_urls = [base_url + state + '.json']

        # This is where the urls get scraped
        counties = get_contents_of_urls(state_urls)
        return render_to_response('scraper/geodata.html', {'counties': counties})

    # If the request is not a GET, just refresh the page
    return render_to_response('scraper/home.html', {'username': request.user.username, 'states': models.states})
