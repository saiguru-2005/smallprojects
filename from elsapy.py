from elsapy.elsclient import ElsClient
from elsapy.elssearch import ElsSearch


API_KEY = "a03b8280429eb6dbe442085ad18b5095"

client = ElsClient(API_KEY)

def fetch_scopus_publications(query, start_year, end_year):
    search = ElsSearch(f'TITLE-ABS-KEY("{query}") AND PUBYEAR AFT {start_year} AND PUBYEAR BEF {end_year}', 'scopus')
    search.execute(client)

    for doc in search.results:
        print("-" * 50)
        if 'dc:title' in doc:
            print(f"Title: {doc['dc:title']}")
        else:
            print("Title: Not available")
        
        if 'prism:coverDate' in doc:
            print(f"Year: {doc['prism:coverDate'][:4]}")
        else:
            print("Year: Not available")
        
        if 'prism:publicationName' in doc:
            print(f"Source: {doc['prism:publicationName']}")
        else:
            print("Source: Not available")
        
        if 'prism:doi' in doc:
            print(f"DOI: {doc['prism:doi']}")
        else:
            print("DOI: Not available")

# Example usage
fetch_scopus_publications("Ensemble Classifier Explainable AI Heart Disease", 2018, 2023)