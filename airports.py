import glob

class Airports():
    """ """
    def find_airport(self, icao):
        search_result = glob.glob("airac/SidStars/{}.txt".format(icao))

        if len(search_result) > 0:
            return search_result[0]
        else:
            return None
    
    def open_airport_file(self, file_location):
        file = open(file_location, 'r')

        return file

    def get_file_section(self, file, section):
        if section == 'SIDS':
            return file.split(section)[1].split('ENDSIDS')[0]

    def parse_section_sids(self, sid_section):
        return sid_section.split("\n")[1].split("\n")[0]

#with open('teste.txt', 'w') as file:
#    file.write(Airports().parse_section_sids(Airports().get_file_section(Airports().open_airport_file(Airports().find_airport("LPPT")).read(), 'SIDS')))