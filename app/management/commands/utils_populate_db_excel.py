import string
from openpyxl import load_workbook

from django.conf import settings
from django.core.management.base import NoArgsCommand

from app.models import Category, Provider


#remov_non_ascii = lambda s: str(filter(lambda x: x in string.printable, s))
remov_non_ascii = lambda s: ''.join(list(filter(lambda x: x in string.printable, s)))

col2num = lambda col: reduce(lambda x, y: x*26 + y, [ord(c.upper()) - ord('A') + 1 for c in col])


def add_category(name):
    """
        If category already exist create it else update it.
    """
    c = Category.objects.get_or_create(name=name)[0]
    return c
    
def add_provider(kwargs):
    """
        This function takes key word argument dictionary of model fields,
        and assign the to provider objects and create it if not exists.
    """
    p = Provider.objects.get_or_create(provider_name=kwargs['provider_name'], 
                                       location_name=kwargs['location_name'])[0]
    p.website=kwargs['website']
    p.address1=kwargs['address1']
    p.address2=kwargs['address2']
    p.city=kwargs['city']
    p.state=kwargs['state']
    p.zipcode=kwargs['zipcode']
    p.contact=kwargs['contact']
    p.phone=kwargs['phone']
    p.hours=kwargs['hours']
    p.save()
    p.category.add(*Category.objects.filter(name__in=kwargs['categories']))
    return p
    
    
def get_sheet_headers(phc_th_sheet):
    """
        This function identifies sheet header blue/orange columns, which 
        are further classfied as categories and provider columns.
    """
    flag = False
    pflag = False
    category_header = dict()
    provider_header = dict()
    
    for cell in phc_th_sheet.rows[0]:
        if not cell.value:
            continue
        if 'provider' in cell.value.lower() and cell.value.lower() != 'categories':
            pflag = True
        if cell.value.lower() == 'categories':
            flag = True
            pflag = False
            continue
        cell_value = remov_non_ascii(cell.value).replace(' ', '_').lower()
        if flag:
            category_header[cell.column] = cell_value
        if pflag:
            provider_header[cell.column] = cell_value
                
    return (provider_header, category_header)
    
    
def populate_categories(category_header):
    """
        This function iterate through dictionary of category and creates them.
    """
    for category_col, category_name in category_header.items():
        add_category(category_name)
        

def populate_providers(phc_th_sheet, provider_header, category_header):   
    """
        This function iterate through dictionary of provider and creates them.
    """
    for sheet_row in phc_th_sheet.rows[1:]:
        attrs = dict(categories=[])
        for cell in sheet_row:
            if cell.column in provider_header:
                attrs[provider_header[cell.column]] = cell.value or ''
            elif cell.column in category_header:
                if not cell.value:
                    continue
                if remov_non_ascii(cell.value).lower() == 'y':
                    attrs['categories'].append(category_header[cell.column])
        add_provider(attrs)


class Command(NoArgsCommand):
    help = 'Read Excel File, find out categories and provides from it and populate in db'

    def handle_noargs(self, **options):
        try:
            phc_th_file = load_workbook(settings.PHC_TH_DATA_FILE_PATH)
            phc_th_sheet = phc_th_file[phc_th_file.get_sheet_names()[0]]
            
            provider_header, category_header = get_sheet_headers(phc_th_sheet)
            print ("Successfully, parsed excel file.")
            
            populate_categories(category_header)
            print ("Successfully, created/updated categories.")
            
            populate_providers(phc_th_sheet, provider_header, category_header)
            print ("Successfully, created/updated providers.")
            
        except IOError:
            print ("Sorry, Unable to open data file to parse and upload data in db.")
            print ("Please fix the file path in project's settings.")
        
        except Exception as ex:
            print ("Oops Sorry! Something went seriously Wrong. Please contact administrator")
            print ("Reason: %s" % repr(ex))
        
