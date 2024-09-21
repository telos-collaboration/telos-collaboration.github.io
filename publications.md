---
layout: default
title: TELOS Publications
image: taipei
mathjax: yes
---

<h2>Publications</h2>

{% assign publicationsSorted = site.data.publications | sort: "created" %}

{% for category in site.data.publication_types %}
<h3>{{ category }}</h3>
<ul class="publication-list">
{% for publication in publicationsSorted reversed %}
{% if publication.category == category %}
<li class="publication">
<span class="publication-title">{{ publication.title }}</span>
<span class="author-list">
{% for author in publication.authors %}
 {{ author }}{% if forloop.last %}{% else %}, {% endif %}
{% endfor %}
</span>
{% if publication.doi %}
<span class="journal-reference">
<a href="https://doi.org/{{ publication.doi }}">
{{ publication.journal_title }}
{{ publication.journal_volume }}
({{ publication.journal_year }})
{{ publication.journal_artid }}
</a>
</span>
{% endif %}
<span class="links">
<a href="https://arxiv.org/abs/{{ publication.arxiv_id }}">arXiv:{{ publication.arxiv_id }} [{{ publication.arxiv_cat }}]</a> •
<a href="{{ publication.inspire }}">INSPIRE-HEP</a>
{% if publication.data %}
 • <a href="{{ publication.data }}">Data</a>
{% endif %}
{% if publication.workflow %}
 • <a href="{{ publication.workflow }}">Workflow</a>
{% endif %}
</span>
</li>
{% endif %}
{% endfor %}
</ul>
{% endfor %}
