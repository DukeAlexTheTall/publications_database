import pandas as pd

def author(df, auth_dict):
    global publishings
    publishings = publishings.append(auth_dict, ignore_index=True)

def save_author(df):
    global publishings
    publishings.to_csv('authors.csv')

def delete_author(author_name):
    publishings.drop([publishings.name == author_name])

publishings = pd.DataFrame(columns=['name','publication_name', 'link_to_publication_page', 'co_authors_of_publication',
                                    'source_of_publication', 'language_of_publication', 'type_of_publication', 
                                    'summary', 'date'])

Sagan = {"name": "Carl Sagan",  "publication_name": "The Space", "link_to_publication_page":None,
         "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication":"eng",
         "type_of_publication":"Sci-Fi", "summary":None, "date":"20-10-93"}

Clark = {"name": "Artur Clark", "publication_name": "Thinks", "link_to_publication_page":None,
         "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication":"eng", 
         "type_of_publication":"Science", "summary":None, "date":"10-01-87"}

Homer = {"name":"Homer Simpson", "publication_name": "Homeless", "link_to_publication_page":"www.simpworld.com/id123",
         "co_authors_of_publication":"Bart Simpson", "source_of_publication":None, "language_of_publication": "eng",
         "type_of_publication":"Survival", "summary":None, "date":"06-06-06"}

Sagan02 = {"name":"Carl Sagan", "publication_name":"Stars", "link_to_publication_page":None,
           "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication": "eng", 
           "type_of_publication": "Sci-Fi", "summary":None, "date":"21-11-19"}

Sagan03 = {"name":"Carl Sagan", "publication_name":"Robotic Manual", "link_to_publication_page":None,
           "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication": "eng",
           "type_of_publication": "Science", "summary":None, "date":"19-05-11"}

Clark02 = {"name":"Artur Clark", "publication_name":"About Me", "link_to_publication_page":None,
           "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication": "eng", 
           "type_of_publication": "Biography", "summary":None, "date":"03-11-78"}

Pierre = {"name":"Jozeph Pierre", "publication_name":"Le Monde", "link_to_publication_page":None,
           "co_authors_of_publication":None, "source_of_publication":None, "language_of_publication": "fr", 
           "type_of_publication": "Science", "summary":None, "date":"08-10-92"}


author(publishings, Sagan)
author(publishings,Clark)
author(publishings,Homer)
author(publishings,Sagan02)
author(publishings,Sagan03)
author(publishings,Clark02)
author(publishings,Pierre)
save_author(publishings)

print(publishings)
