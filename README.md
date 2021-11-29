# Wiki

*This project is an implementation of a Wiki encyclopedia.*

It will consist of the following:
 - **Entry page**:
    - Visiting /wiki/TITLE, where TITLE is the title of an encyclopedia entry, should render a page that displays the contents of that encyclopedia entry. 
 - **Index page**:
    - Lists names of all pages in the encyclopedia which send user to the corresponding page when clicked upon.
 - **Search**:
    - Allow the user to type a query into the search box in the sidebar to search for an encyclopedia entry. 
 - **New Page**:
    - Clicking “Create New Page” in the sidebar should take the user to a page where they can create a new encyclopedia entry. 
 - **Edit Page**[^extra]:
    - On each entry page, the user should be able to click a link to be taken to a page where the user can edit that entry’s Markdown content in a textarea. 
 - **Random Page**[^extra]:
    - Clicking “Random Page” in the sidebar should take user to a random encyclopedia entry.
 
[^extra]: These are not part of the main plan and are just extra ideas we *might* implement.

## Getting Started

TODO: Describe steps to install requirements and get the application running.
- To add a new page, we need to:
    - Add its markdown to *entries*.
    - Add its path to url_patterns in urls.py using include()
    
