---
layout: default
title: TELOS Acknowledgement Generator
image: tsukuba
---

<style>
label {
  display: inline-block;
  padding-right: 10px;
  white-space: nowrap;
}
input {
  vertical-align: middle;
}
label span {
  vertical-align: middle;
}
</style>

# TELOS Acknowledgement Generator

Use this page to generate acknowledgments for TELOS publications.

<h4>People</h4>

{% for member_group in site.data.member_groups %}
<h5>{{ member_group }}</h5>
<div>
{% for member in site.data.members %}
{% if member.status == member_group %}
<label for="{{ member.name }}">
<input type="checkbox" id="{{ member.name }}" value="{{ member.name }}" />
<span>{{ member.name }}</span>
</label>
{% endif %}
{% endfor %}
</div>
{% endfor %}

<h5>Others</h5>
{% for member in site.data.members %}
{% unless site.data.member_groups contains member.status %}
<label for="{{ member.name }}">
<input type="checkbox" id="{{ member.name }}" value="{{ member.name }}" />
<span>{{ member.name }}</span>
</label>
{% endunless %}
{% endfor %}

<h4>Computers</h4>

<h4>Other attributes</h4>

<p>Include grants active between</p>

<label>
Start date
<input type="date" id="startDate" name="startDate" />
</label>

<label>
End date
<input type="date" id="endDate" name="startDate" />
</label>

<h3>Acknowledgement</h3>

<p id="people-acknowledgement"></p>
<p id="computing-acknowledgement"></p>



<script>
  members = JSON.parse(decodeURIComponent("{{ site.data.members | jsonify | uri_escape }}"));
  grants = JSON.parse(decodeURIComponent("{{ site.data.acknowledgements | jsonify | uri_escape }}"));
  sponsors = JSON.parse(decodeURIComponent("{{ site.data.sponsors | jsonify | uri_escape }}"));
  
  const getInitials = function (author) {
    fullAuthor = members.find(member => member.name === author);
    if (fullAuthor != undefined && Object.hasOwn(fullAuthor, "initials")) {
      return fullAuthor.initials.replaceAll("-", ".-").replaceAll(" ", ".~") + ".";
    } else {
      return author.split(" ").map(name => name[0]).join(".~") + ".";
    }
  }

  const formatAuthorList = function (authors) {
    var authorList = []
    if (authors.length == 2) {
      return getInitials(authors[0]) + " and " + getInitials(authors[1]);
    }
    for (const author of authors) {
      if (author === authors[authors.length - 1]) { 
        authorList.push("and " + getInitials(author))
      } else {
        authorList.push(getInitials(author));
      }
    }
    return authorList.join(", ");
  };

  const formatSingleGrant = function (grant, authors) {
    const authorList = formatAuthorList(authors);
    return [
      grant.organisation,
      (
        grant
        .text
        .replaceAll("{fundees}", authorList)
        .replaceAll("{code}", grant.code)
        .replaceAll("{is}", authors.length == 1 ? "is" : "are")
        .replaceAll("{s}", authors.length == 1 ? "s" : "")
      )
    ]
  };
  
  const getOrganisation = function (organisationAcronym, organisations) {
    // Using findIndex here means that
    // if there is a duplicate definition, it will be ignored
    matchOrganisation = organisations.findIndex(
      ((organisation) => organisation.acronym == organisationAcronym )
    );
    if (matchOrganisation < 0) {
      return [organisationAcronym, organisations];
    }
    if (organisations[matchOrganisation].defined) {
      return [organisationAcronym, organisations];
    }
    organisations[matchOrganisation].defined = true;
    return [organisations[matchOrganisation].text + " (" + organisationAcronym + ")", organisations];
  }
  
  const combineFormattedGroup = function (formattedGroup) {
    if (formattedGroup.length == 1) {
      return formattedGroup[0].replaceAll("{grant_plural}", "");
    } else if (formattedGroup.length == 2) {
      return formattedGroup.join(" and ").replace("{grant_plural}", "s");
    } else {
      return (
        formattedGroup.slice(0, -1).join(", ") + " and " + formattedGroup.at(-1)
      ).replaceAll("{grant_plural}", "s");
    }
  }

  const formatAuthorGroupGrants = function (grants, authors, organisations) {
    const acknowledgements = grants.map(grant => formatSingleGrant(grant, authors));
    var formattedAcknowledgements = [];
    var groupCount = 0;
    var formattedOrganisation = "";
    if (acknowledgements[0][1].includes("{organisation}")) {
      [formattedOrganisation, organisations] = getOrganisation(acknowledgements[0][0], organisations);
    }
    var also = "";
    var formattedGroup = [acknowledgements[0][1].replaceAll("{organisation}", formattedOrganisation).replaceAll("{also}", also)];
    var previousCommonWords = 0;
    var wordIdx = 0;
    for (let acknowledgementIdx = 1; acknowledgementIdx < acknowledgements.length; acknowledgementIdx++) {
      const currentAcknowledgement = acknowledgements[acknowledgementIdx][1].split(" ");
      const previousAcknowledgement = acknowledgements[acknowledgementIdx - 1][1].split(" ");
      var combine = false;
      for (wordIdx = 0; wordIdx < currentAcknowledgement.length; wordIdx++) {
        const word = currentAcknowledgement[wordIdx];
        const previousWord = previousAcknowledgement[wordIdx];
        if (word != previousWord) {
          break;
        }
        if (word == "{organisation}" && acknowledgements[acknowledgementIdx][0] != acknowledgements[acknowledgementIdx - 1][0]) {
          break;
        }
        if (word.toLowerCase() != "the") {
          combine = true;
        }
      }
      if (combine && wordIdx > 2 && wordIdx >= previousCommonWords && currentAcknowledgement.findIndex((a) => a.includes("{grant_plural}")) < wordIdx) {
        const currentFragment = currentAcknowledgement.slice(wordIdx).join(" ");
        var currentOrganisation;
        if (currentFragment.includes("{organisation}")) {
          [currentOrganisation, organisations] = getOrganisation(acknowledgements[acknowledgementIdx][0], organisations);
        }
        formattedGroup.push(currentFragment.replaceAll("{organisation}", currentOrganisation).replaceAll("{also}", also));
        previousCommonWords = wordIdx;
      } else {
        formattedAcknowledgements.push(combineFormattedGroup(formattedGroup));
        also = "also";
        const currentFragment = currentAcknowledgement.join(" ");
        if (currentFragment.includes("{organisation}")) {
          [currentOrganisation, organisations] = getOrganisation(acknowledgements[acknowledgementIdx][0], organisations);
        }
        formattedGroup = [currentFragment.replaceAll("{organisation}", currentOrganisation).replaceAll("{also}", also)];
        previousCommonWords = 0;
      }
    }
    formattedAcknowledgements.push(combineFormattedGroup(formattedGroup));
    return [formattedAcknowledgements.join(". ") + ". ", organisations];
  };
  
  const getAcknowledgement = function (authors, grants, sponsors) {
    var acknowledged = [];
    var acknowledgement = [];
    authors = authors.toSorted((name1, name2) => {
      const surname1 = name1.split(" ").reverse()[0];
      const surname2 = name2.split(" ").reverse()[0];
      if (surname1 < surname2) {return -1;}
      if (surname2 > surname1) {return 1;}
      return 0;
    });
    var groupAcknowledgement;
    for (const author of authors) {
      while ((toAcknowledge = grants.filter(grant => grant.fundees.includes(author) & !acknowledged.includes(grant.name))).length > 0) {
        groupAuthors = authors.filter(singleAuthor => toAcknowledge[0].fundees.includes(singleAuthor)).toSorted();
        groupGrants = grants.filter(grant => grant.fundees.filter(fundee => authors.includes(fundee)).toSorted().toString() === groupAuthors.toString());
        [groupAcknowledgement, sponsors] = formatAuthorGroupGrants(groupGrants, groupAuthors, sponsors);
        acknowledgement.push(groupAcknowledgement);
        for (acknowledgedGrant of groupGrants) {
          acknowledged.push(acknowledgedGrant.name);
        }
      }
    }
    return acknowledgement.join(" ");
  };

  const generate = function () {
    document.getElementById("computing-acknowledgement").textContent = "TODO: implement computing acknowledgement.";

    const authors = document.querySelectorAll("input[type=checkbox]").values().filter(c => c.checked).map(c => c.value).toArray();
    const startDate = document.getElementById("startDate").valueAsDate;
    const endDate = document.getElementById("endDate").valueAsDate;

    const author_grants = grants.filter(grant => (grant.fundees.filter(fundee => authors.includes(fundee)).length > 0));
    const target_grants = author_grants.filter(grant => (Date.parse(grant.start) <= endDate & Date.parse(grant.end) >= startDate));
  
    document.getElementById("people-acknowledgement").textContent = getAcknowledgement(authors, target_grants, sponsors);
  }

  for (const element of document.querySelectorAll("input")) {
    element.addEventListener("input", (event) => generate());
  }

{% for member in site.data.members %}
{% if member.status == "Core Members" %}
  document.getElementById("{{ member.name }}").checked = true;
{% endif %}
{% endfor %}


  document.getElementById("startDate").valueAsDate = new Date();
  document.getElementById("endDate").valueAsDate = new Date();
  generate();
</script>
