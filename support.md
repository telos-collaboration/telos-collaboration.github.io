---
layout: default
title: TELOS Supporters
image: tsukuba
---

<p>Our work would not be possible without the generous support of many organisations.</p>

{% assign sponsorsSorted = site.data.sponsors | sort: "text" %}

{% for sponsor_group in site.data.sponsor_groups %}
<h2>{{ sponsor_group.title }}</h2>

<p>{{ sponsor_group.description }}</p>

<div class="supporter-list">
{% for sponsor in sponsorsSorted %}
{% if sponsor.group == sponsor_group.id %}
<div class="supporter-entry">
<img class="supporter-logo" src="/assets/img/sponsors/{{ sponsor.image }}" alt="{{ sponsor.text }}">
<p class="supporter-text">
{% if sponsor.link %}<a href="{{ sponsor.link }}">{% endif %}
{{ sponsor.text }}
{% if sponsor.link %}</a>{% endif %}
</p>
</div>
{% endif %}
{% endfor %}
</div>
{% endfor %}
