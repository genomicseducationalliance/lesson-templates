#!/usr/bin/env python3

import argparse
import csv
from jinja2 import Environment, FileSystemLoader

def main():
    
    def gettemplate(template_dir, template_name):
        """get the template location and name to load into the Jinja functions"""
        file_loader = FileSystemLoader(template_dir) 
        env = Environment(loader=file_loader)
        return env.get_template(template_name)
    
    
    #open the txt file (tab separated entries) and print template
    
    def renderfromcsv(tab_delimited_file,outfile,gettemplate):
        """ Imports a CSV file as a dictionary - headers are keys; print into the jinja template"""
        # indicate a new dialect with \t as the delimiter
        csv.register_dialect("tab-delimited", delimiter="\t")
        # use the utf-8-sug to get rid of pesky byte encoding characters 
        with open(tab_delimited_file, "rt", encoding="latin-1") as file:
            # read data into a dictionary
            reader=csv.DictReader(file,dialect="tab-delimited")
            for values in reader:
                gen_template = gettemplate(template_dir, template_name)
                output = gen_template.render(values)
                # substitue into jinja template
            with open(outfile, 'w') as outfile:
                print(output, file=outfile)   
    

    renderfromcsv(tab_delimited_file,outfile,gettemplate)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Move data from a tab delimited file into a ReStructured Text Jinja2 Template")
    parser.add_argument('--template-dir', '-d' , dest="template_dir", type=str, nargs=1, help="directory path where template file is located", required=True)
    parser.add_argument('--template-name', '-t' , dest="template_name", type=str, nargs=1, help="name of template file", required=True)
    parser.add_argument('--tab-delimited-file', '-c', dest="tab_delimited_file", type=str, nargs=1, help="path to the tab delimited file", required=True)
    parser.add_argument('--outfile', '-o', dest="outfile",type=str, nargs=1, help="name and path for output file", required=True)
    args = parser.parse_args()    
    template_dir=args.template_dir[0]
    template_name=args.template_name[0]
    tab_delimited_file=args.tab_delimited_file[0]
    outfile=args.outfile[0]
    print(template_dir,template_name,tab_delimited_file,outfile)
    main()

