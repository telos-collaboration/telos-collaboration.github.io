#!/usr/bin/env python3

from argparse import ArgumentParser, FileType
import requests
import yaml

parser = ArgumentParser()
parser.add_argument("output_file", type=FileType("w"), default="-"),
args = parser.parse_args()

response = requests.get(
    r"https://inspirehep.net/api/literature?sort=mostrecent&size=100&q=author%3Apiai%20author%3Ahong%20author%3Alin%20author%3Alucini"
)
publication_metadata = response.json()["hits"]["hits"]

def categorise(pub):
    if "publication_info" not in pub["metadata"]:
        return "Preprints"
    elif "journal_title" not in pub["metadata"]["publication_info"][0]:
        return "Conference proceedings"
    elif pub["metadata"]["publication_info"][0]["journal_title"] in ["PoS", "EPJ Web Conf."]:
        return "Conference proceedings"
    elif pub["metadata"]["publication_info"][0]["journal_title"] in ["Phys.Lett.B", "Phys.Rev.D", "Universe", "JHEP"]:
        return "Journal articles"
    else:
        raise ValueError(f"{pub['metadata']['publication_info'][0]['journal_title']} not recognised")


def journal_info(pub):
    if "publication_info" not in (metadata := pub["metadata"]):
        return {}
    if "journal_title" not in (pubinfo := metadata["publication_info"][0]):
        return {"journal": "tbc"}
    return {
        "journal_title": pubinfo["journal_title"],
        "journal_volume": pubinfo["journal_volume"],
        "journal_year": pubinfo["year"],
        "journal_artid": pubinfo["artid"],
    }

publications = [
    {
        **{
            "authors": [f"{author['first_name']} {author['last_name']}" for author in pub["metadata"]["authors"]],
            "arxiv_id": pub["metadata"]["arxiv_eprints"][0]["value"],
            "arxiv_cat": pub["metadata"]["arxiv_eprints"][0]["categories"][0],
            "title": pub["metadata"]["titles"][0]["title"],
            "data": "tbc",
            "workflow": "tbc",
            "inspire": f"https://inspirehep.net/literature/{pub['id']}",
            "category": categorise(pub),
            "created": pub["created"],
            "doi": pub["metadata"]["dois"][0]["value"] if "dois" in pub["metadata"] else None,
        },
        **journal_info(pub),
    }
    for pub in publication_metadata
]

print(yaml.dump(publications), file=args.output_file)
