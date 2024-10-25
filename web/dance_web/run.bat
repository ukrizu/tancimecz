{% extends "base.html" %}
{% load custom_filters %}
{% load static %}

{% block title %}Homepage{% endblock %}

{% block extra_css %}
    <link rel="stylesheet" type="text/css" href="{% static 'css/homepage.css' %}">
{% endblock %}

{% block content %}
    <div class="title">
        <h1>TANCE UNIVERZÁLNÍHO MÍRU</h1>
    </div>
    <div class="o_tancich">
        <h2>O tancích</h2>
        <p>Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Sed ac dolor sit amet purus malesuada congue. Sed elit dui, pellentesque a, faucibus vel, interdum nec, diam. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur? Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. </p>
        <a href="#o-tancich"><button type="submit" class="button">Více</button></a>
    </div>
    <div class="workshops">
        <h2>WORKSHOPY</h2>
        <div class="events">
            {% for event in events|filter_by_type:2|filter_past_events|slice:":2" %}
                <div class="event">
                    <div class="event-title">
                        {{ event.title }}
                    </div>
                    <div class="image">
                        <img src="{{ event.image.url }}">
                    </div>
                    <div class="event-details">
                        <div class="event-link">
                            {% if event.link %}
                            <p><a href="{{ event.link }}" target="_blank">{{ event.link }}</a></p>
                            {% endif %}
                        </div>
                        <div class="event-date">
                            {% with event|date_format as date %}
                                <p>{{ date.day }} {{ date.date }} <br>{% if date.time %} {{ date.time }} {% endif %}</p>
                            {% endwith %}
                        </div>
                        <div class="event-location">
                            <p><strong>Kde: </strong>{{ event.location.town }}, {{ event.location.address }}</p>
                            <div class="event-location-description"> 
                                {% if event.location.description %}
                                    <p>{{ event.location.description }}</p>
                                {% endif %}
                            </div> 
                        </div>
                        <div class="event-lector">
                            <p><strong>S kým: </strong>
                                {% for lector in event.lector.all %}
                                    <a href="{% url 'lector_page' slug=lector.slug %}">
                                        {{ lector.firstName }}{% if lector.lastName %} {{ lector.lastName }}{% endif %}{% if not forloop.last %}, {% endif %}
                                    </a>
                                {% endfor %}
                            </p>
                        </div>
                        <div class="event-price">
                            {% if event.price %}
                                <p><strong>Cena: </strong>{{ event.price }}</p>
                            {% endif %}
                        </div>
                        <div class="event-contact">
                            <p><strong>Kontakt: </strong><small>{{ event.contact }}</small></p>
                        </div>
                        <div class="event-description">
                            <p class="description"><strong>Na co se těšit: </strong>{{ event.description }}</p>
                            <button class="toggle-description">↓</button>
                        </div>
                    </div>
                </div>
            {% endfor %}
            {% if not eventsevents|filter_by_type:2|filter_past_events %}
                <p>Momentálně nejsou žádné workshopy.</p>
            {% endif %}
            </div>
            <div class="all">
                <form method="get" action="{% url 'events' %}">
                    <button type="submit" class="button">Všechny</button>
                </form>
            </div>
    </div>
    <div class="vecerni-akce">
        <h2>Večerní akce</h2>
        <div class="events">
            {% for event in events|filter_by_type:1|filter_past_events|slice:":2" %}
                <div class="event">
                    <div class="event-title">
                        {{ event.title }}
                    </div>
                    <div class="image">
                        <img src="{{ event.image.url }}">
                    </div>
                    <div class="event-details">
                        <div class="event-link">
                            {% if event.link %}
                            <p><a href="{{ event.link }}" target="_blank">{{ event.link }}</a></p>
                            {% endif %}
                        </div>
                        <div class="event-date">
                            {% with event|date_format as date %}
                                <p>{{ date.day }} {{ date.date }} <br>{% if date.time %} {{ date.time }} {% endif %}</p>
                            {% endwith %}
                        </div>
                        <div class="event-location">
                            <p><strong>Kde: </strong>{{ event.location.town }}, {{ event.location.address }}</p>
                            <div class="event-location-description"> 
                                {% if event.location.description %}
                                    <p>{{ event.location.description }}</p>
                                {% endif %}
                            </div> 
                        </div>
                        <div class="event-lector">
                            <p><strong>S kým: </strong>
                                {% for lector in event.lector.all %}
                                    <a href="{% url 'lector_page' slug=lector.slug %}">
                                        {{ lector.firstName }}{% if lector.lastName %} {{ lector.lastName }}{% endif %}{% if not forloop.last %}, {% endif %}
                                    </a>
                                {% endfor %}
                            </p>
                        </div>
                        <div class="event-price">
                            {% if event.price %}
                                <p><strong>Cena: </strong>{{ event.price }}</p>
                            {% endif %}
                        </div>
                        <div class="event-contact">
                            <p><strong>Kontakt: </strong><small>{{ event.contact }}</small></p>
                        </div>
                        <div class="event-description">
                            <p class="description"><strong>Na co se těšit: </strong>{{ event.description }}</p>
                            <button class="toggle-description">↓</button>
                        </div>
                    </div>
                </div>
            {% endfor %}
            {% if not eventsevents|filter_by_type:2|filter_past_events %}
                <p>Momentálně nejsou žádné večerní tance.</p>
            {% endif %}
            </div>
            <div class="all">
                <form method="get" action="{% url 'events' %}">
                    <button type="submit" class="button">Všechny</button>
                    </form>
        </div>
    </div>
    <div class="o_tancich" id="o-tancich">
    <h2>O tancích</h2>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean congue semper aliquam. Sed lacinia viverra ante id dictum. Sed rutrum ante sed venenatis congue. Cras a leo ac dolor consequat mattis. Maecenas sed felis at magna ullamcorper varius. Sed eu sapien ut tortor consectetur auctor ut ac felis. Mauris enim mauris, faucibus ac interdum et, tempus vitae augue. Vivamus feugiat nisl eu arcu ultrices, eu pharetra quam aliquam.

        <p>Donec at risus ac leo luctus tincidunt id eu mauris. Aenean bibendum ex sit amet nisl hendrerit sollicitudin. Vivamus malesuada enim at est sagittis pellentesque. Phasellus id mollis nisl. Pellentesque aliquet magna ut sapien scelerisque tincidunt. Sed dui sapien, condimentum quis lacinia mattis, bibendum eu ante. Sed eget est sed augue varius euismod at et lectus. Nam sed lectus et felis aliquam interdum. Etiam risus lacus, tristique sit amet nisi id, pharetra consequat dui. Pellentesque eleifend convallis sapien, a sagittis ipsum suscipit vel. Etiam tincidunt facilisis neque, nec vehicula enim consectetur vel. Vivamus pulvinar suscipit eros, eget cursus nisi aliquet non.

        <p>Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Mauris et faucibus metus. Nunc malesuada diam et felis dictum, in iaculis dolor mollis. Maecenas velit nibh, ultrices et pulvinar sit amet, tincidunt nec massa. Sed quis consectetur odio. Aenean dictum laoreet eros eu commodo. Duis pellentesque dictum tempus. Quisque nibh ex, posuere ac facilisis ut, viverra quis ante. Duis sodales tempus urna, eget dignissim massa egestas nec. Suspendisse sollicitudin sem in molestie maximus. Proin ac nibh ligula.</p></p>
    </div>
    <div class="all">
        <form method="get" action="{% url 'o_tancich' %}">
            <button type="submit" class="button">Vše o tancich</button>
            </form>
    </div>
    <h2>Naši lektoři:</h2>
    <div class="lectors">
        {% for lector in lectors %}
        <div class="lector">
            <a href="{% url 'lector_page' slug=lector.slug %}">
                <img src="{{ lector.image.url }}" alt="{{ lector.firstName }}">
            </a>
        </div>
        {% endfor %}
        {% if not lectors %}
            <p>No lectors available.</p>
        {% endif %}
    </div>
    <div class="all">
        <form method="get" action="{% url 'lectors' %}">
            <button type="submit" class="button">Seznam lektorů</button>
        </form>
    </div>
    <div class="o_nas">
        <h2>O nás</h2>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam dolor mauris, bibendum nec ante quis, lobortis placerat sem. Vivamus lectus neque, semper eu ipsum sed, gravida aliquet odio. Nam placerat, nulla sed maximus ullamcorper, leo felis aliquet lacus, sollicitudin eleifend justo orci ut velit. Curabitur semper sagittis ligula a ultrices. Morbi metus purus, ornare eu ligula at, tincidunt luctus nulla. Curabitur dignissim id enim id consectetur. Donec finibus ut elit non ornare. Sed id odio ut velit feugiat semper eget non ante. Cras ultrices efficitur eros, in maximus sapien posuere sit amet. Donec ipsum metus, sodales tristique sollicitudin nec, tincidunt at risus. Vivamus condimentum, magna et blandit vestibulum, quam nulla sagittis mi, sed interdum urna diam vel sem. Aliquam scelerisque eget est a hendrerit.

            <p>Nullam mollis magna sed risus elementum, quis feugiat sapien auctor. Cras at elementum turpis. Phasellus a eros velit. Ut mollis pellentesque ex id euismod. Donec pretium dolor sit amet mi pharetra, eget cursus turpis ultrices. Sed molestie magna erat, vel fermentum justo scelerisque id. Curabitur ultrices eros a ipsum sodales vulputate. Maecenas quis metus aliquam, venenatis elit eget, tempor odio. Praesent egestas ipsum quis nunc gravida, at efficitur nisi pellentesque. Sed ac auctor ligula, in vehicula.</p></p>
    </div>
    <div class="all">
        <form method="get" action="{% url 'o_nas' %}">
            <button type="submit" class="button">Více</button>
            </form>
    </div>
    <div class="oraganizace">
        <h2>Organizace:</h2>
        <p>loga</p>
    </div>
    {% endblock %}




