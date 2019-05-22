#!/usr/bin/env python3

import argparse
import csv
from jinja2 import Environment, FileSystemLoader

def main():
    
    def excelcsvtopipe(csv_file):
        """Converts an Excel comma-delimited csv file to pipe-delimited"""
        with open(csv_file, "rt", encoding="utf8") as file:
            reader = csv.reader(file)
            for rows in reader:
                writer=csv.writer(open('temp.csv','w'),delimiter='|')
                writer.writerow(rows)
                  
    
    
    def gettemplate(template_dir, template_name):
        """get the template location and name to load into the Jinja functions"""
        file_loader = FileSystemLoader(template_dir) 
        env = Environment(loader=file_loader)
        return env.get_template(template_name)
    
    
    #open the csv file and print template
    
    def renderfromcsv(tempfile,outfile,gettemplate):
        """ Imports a CSV file as a dictionary - headers are keys; print into the jinja template"""
        reader = csv.reader(open(tempfile, "rt"),delimiter="|")
        reader2=csv.DictReader(reader)
        for values in reader: 
            gen_template = gettemplate(template_dir, template_name)
            output = gen_template.render(values)
        with open(outfile, 'w') as outfile:
            print(output, file=outfile)   
    
    excelcsvtopipe(csv_file)
    renderfromcsv(tempfile,outfile,gettemplate)

if __name__ == '__main__':
    parser=argparse.ArgumentParser(description="Move data from a CSV file into a ReStructured Text Jinja2 Template")
    parser.add_argument('--template-dir', '-d' , dest="template_dir", type=str, nargs=1, help="directory path where template file is located", required=True)
    parser.add_argument('--template-name', '-t' , dest="template_name", type=str, nargs=1, help="name of template file", required=True)
    parser.add_argument('--csv-file', '-c', dest="csv_file", type=str, nargs=1, help="path to the csv file", required=True)
    parser.add_argument('--outfile', '-o', dest="outfile",type=str, nargs=1, help="name and path for output file", required=True)
    args = parser.parse_args()    
    template_dir=args.template_dir[0]
    template_name=args.template_name[0]
    csv_file=args.csv_file[0]
    outfile=args.outfile[0]
    tempfile='temp.csv'
    main()

