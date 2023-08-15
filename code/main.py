import xml.etree.ElementTree as ET


def read_xml_file(file_path):
    """  
    Read the xml file and retunr the tree value

    Parameters
        ----------
        file_path : input xml file path

    Returns
        -------
        return the xml tree values  
    """
    tree = ET.parse(file_path)
    return tree.getroot()


def write_ouput_file(file_path, data):
    """  
    Write the data to the target out file

    Parameters
        ----------
        file_path : output text file path
    data : Contains the Subsumption Hierarchy data 

    Returns
        -------
        Write the subsumption hierachy data to the ouput file   
    """

    # open the text file with write permission
    file = open(file_path, 'w')

    # write the data of class and sub class data to the file
    for key in data:
        file.write('Class: ' + key + '\n')
        set_data = data[key]
        list_data = list(set_data)

        if bool(set_data):
            file.write("\tSubClassOf: ")
            for item in list_data[:-1]:
                file.write(item+', ')

            file.write(list_data[-1])
            file.write("\n")


def handle_transitivity(dictionary):
    """  
    handle the transitivity of the sub class
    """
    # for transitivity
    dic = {}
    while(dic != dictionary):
        dic = dictionary.copy()
        for key in dictionary:
            news = dictionary[key]
            for item in dictionary[key]:
                if item in dictionary:
                    for i in dictionary[item]:
                        if i in dictionary:
                            news = news.union({i})

            dictionary[key] = news


def main():

    dictionary = {}
    root = read_xml_file("../input/input.xml")

    for child in root.findall("Class"):

        key = child.find('CONCEPT').text  # get the class name as key
        set_data = set()                  # get the subclasses in a set

        # handle  SubClassOf part
        for newChild in child.findall('SubClassOf'):

            #Get the all sub class values
            if(newChild.find('CONCEPT') != None):
                set_data.add(newChild.find('CONCEPT').text)

            #handle the Not subclass case
            if(newChild.find('NOT') != None):
                for notChild in newChild.findall('NOT'):
                    set_data.add("not "+notChild.find('CONCEPT').text)

            #handle the EXISTS case
            if(newChild.find('EXISTS') != None):
                set_data.add(newChild.find('ROLE').text +
                             " some " + newChild.find('CONCEPT').text)
            
            #
            if(newChild.find('AND') != None):
                for newChild in child.findall('EquivalentTo'):
                    if(newChild.find('CONCEPT') != None):
                        set_data.add(newChild.find('CONCEPT').text)

                    if(newChild.find('NOT') != None):
                        for notChild in newChild.findall('NOT'):
                            set_data.add("not "+notChild.find('CONCEPT').text)

                    if(newChild.find('EXISTS') != None):
                        set_data.add(newChild.find('ROLE').text +
                                     " some " + newChild.find('CONCEPT').text)

        # handle Equivalent to part
        for newChild in child.findall('EquivalentTo'):
            if(newChild.find('CONCEPT') != None):
                set_data.add(newChild.find('CONCEPT').text)

            if(newChild.find('NOT') != None):
                for notChild in newChild.findall('NOT'):
                    set_data.add("not "+notChild.find('CONCEPT').text)

            if(newChild.find('EXISTS') != None):
                set_data.add(newChild.find('ROLE').text +
                             " some " + newChild.find('CONCEPT').text)

            if(newChild.find('AND') != None):
                for newnewChild in newChild.findall('AND'):
                    if(newnewChild.find('CONCEPT') != None):
                        set_data.add(newnewChild.find('CONCEPT').text)

                    if(newnewChild.find('NOT') != None):
                        for notChild in newnewChild.findall('NOT'):
                            set_data.add("not "+notChild.find('CONCEPT').text)

                    if(newnewChild.find('EXISTS') != None):
                        set_data.add(newnewChild.find('EXISTS').find(
                            'ROLE').text+" some " + newnewChild.find('EXISTS').find('CONCEPT').text)

        dictionary[key] = set_data

    handle_transitivity(dictionary)  # handle the transitivity
    # write the data to the ouput file
    write_ouput_file("../parser/src/krr/test/input/output.txt", dictionary)

if __name__ == "__main__":

    # calling main function
    main()