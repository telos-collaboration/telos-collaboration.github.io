---
layout: default
title: About the TELOS Collaboration
image: haeundae
---

<p>
    Formed in 2016,
	the TELOS Collaboration performs
	<b>T</b>heoretical <b>E</b>xplorations on the <b>L</b>attice with <b>O</b>rthogonal and <b>S</b>ymplectic groups.
</p>

<h2>Members</h2>

{% assign membersSorted = site.data.members | sort: "name" %}

{%- for category in site.data.member_groups -%}
<h3>{{ category }}</h3>
<div class="member-container">

{%- for member in membersSorted -%}
{%- if member.status == category -%}
<div class="collaboration-member">
{%- if member.image -%}
<img class="collaboration-member-portrait" src="{{ "/assets/img/members/" | append: member.image | append: ".jpg" | relative_url }}" alt="Photograph of {{ member.name }}">
{%- else -%}
<img class="collaboration-member-portrait" src="/assets/img/person.svg" alt="No portrait available">
{%- endif -%}
<p class="collaboration-member-name">
  {{ member.name }}
  {% if member.orcid %}
  <a href="https://orcid.org/{{ member.orcid }}"><img src="/assets/img/orcid.svg" width="22px" style="vertical-align: -10%;" alt="ORCID icon"></a>
  {% endif %}
</p>
{%- if member.affiliation -%}
<p class="collaboration-member-affiliation">
  <a href="{{ member.affiliation-url }}" class="collaboration-member-affiliation-link">{{ member.affiliation }}</a>
</p>
{%- endif -%}
{%- if member.github -%}
<p class="collaboration-member-icons">
  <a href="https://github.com/{{ member.github }}" class="github-link">
    <img src="/assets/img/github.svg" width="24px" style="vertical-align: -10%;"> {{ member.github }}
  </a>
</p>
{%- endif -%}
</div>
{%- endif -%}
{%- endfor -%}
</div>
{%- endfor -%}
