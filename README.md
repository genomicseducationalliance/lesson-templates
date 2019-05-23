# lesson-templates
Templates and tools for creating GEA hosted lessons and documentation

## Going from google form to restructured text

1. Lesson submission will use a form like a google form to enforce controlled
 vocabulary.
2. A single row in the resulting spreadsheet will be a submission. This must be
copied into a sheet with safe column headers (TODO: automate). This two row
spreadsheet is saved as a tab-delimited file.
3. jinja-render.py is called to push the data from the spreesheet into a
restructured text template.
  `python jinja-render.py -d ~/path/to/template -t template.rst -c data.tsv -o rendered.rst`
