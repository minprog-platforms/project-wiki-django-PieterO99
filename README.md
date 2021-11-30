# Wiki

*This project is an implementation of a Wiki encyclopedia.*

It will consist of the following:
 - [ x ] **Entry page**:
    - Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry. Initially the pages will be CSS, Django, Git, HTML and Python, but eventually users will be able to add new pages.
 - [ x ] **Index page**:
    - Lists names of all pages in the encyclopedia which send user to the corresponding page when clicked upon.
 - [ x ] **Search**:
    - Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry. 
 - [ x ] **New Page**:
    - Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry. 
 - [  ] **Edit Page**[^extra]:
    - On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea. 
 - [ x ]**Random Page**[^extra]:
    - Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
 
[^extra]: These are not part of the main plan and are just extra ideas we *might* implement.

## Getting Started

TODO: Describe steps to install requirements and get the application running.
-  To add a new page that is not an entry, we need to add a html representing the page. 
   Then, we need to add a path to urls.py and a function to views.py that tells the path how to translate a request
   to our html page.
   - pages we will need to add:
      -  error.html
      -  new_page.html
      -  results.html (search results)
      -  edit_page.html (if we want to do this extra implementation)
-  To add a new entry page, we need to:
    - Add its markdown to *entries*.
    - When we want the user to be able to add an entry page, we can use the get method of forms
      and util's save_entry function.
    
