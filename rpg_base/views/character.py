from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from rpg_base.models import Character, Campaign


@login_required
def index(request, campaign_pk):
    campaign = get_object_or_404(Campaign, pk=campaign_pk)
    characters = Character.objects.filter(campaign=campaign)
    paginator = Paginator(characters, 25)

    page = request.GET.get('page')

    try:
        characters = paginator.page(page)
    except PageNotAnInteger:
        characters = paginator.page(1)
    except EmptyPage:
        characters = paginator.page(paginator.num_pages)

    context = {
        "objects": characters,
        "campaign": campaign,
    }

    return render_to_response("character/index.html", context)


@login_required
def view(request, campaign_pk, character_pk):
    character = get_object_or_404(Character, pk=character_pk, campaign=campaign_pk)

    context = {
        "character": character,
    }

    return render_to_response("character/view.html", context)
