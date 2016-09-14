try:
    from selenium.common.exceptions import WebDriverException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotVisibleException
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.remote.webelement import WebElement
except ImportError:
    print "Selenium module is not installed...Exiting program."
    exit(1)

##### Element ######

class Element:
    driver = None
    selectedElement = None
    elements = None

    def __init__(self,driver):
        self.driver = driver
        self.elements = None
        self.elements = []
        self.selectedElement = self.findElementByTag('body')

    def dealloc(self):
        if self.driver:
            del self.driver
        if self.elements:
            del self.elements[:]
            del self.elements
        if self.selectedElement:
            del self.selectedElement

    ##### Locating Element #####

    def findElementByID(self,id_str, element = 0):
        if not self.validateLocator(id_str):
            print "Invalid ID: {}".format(id_str)
            return 0
        print "Searching for element by ID: '{}'".format(id_str)
        try:
            if element:
                element = element.find_element_by_id(id_str)
            else:
                element = self.driver.find_element_by_id(id_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by ID '{}'".format(id_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with ID: '{}'".format(id_str)
        else:
            print "Couldn't find element by id '{}'".format(id_str)
            return 0
        return element

    def findElementByName(self,name_str,element=0):
        if not self.validateLocator(name_str):
            print "Invalid Name: {}".format(name_str)
            return 0
        print "Searching for element by Name: '{}'".format(name_str)
        try:
            if element:
                element = element.find_element_by_name(name_str)
            else:
                element = self.driver.find_element_by_name(name_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Name '{}'".format(name_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Name: '{}'".format(name_str)
        else:
            print "Couldn't find element by Name '{}'".format(name_str)
            return 0
        return element

    def findElementByTag(self,tag_str,element=0):
        if not self.validateLocator(tag_str):
            print "Invalid Tag: {}".format(tag_str)
            return 0
        print "Searching for element by Tag: '{}'".format(tag_str)
        try:
            if element:
                element = element.find_element_by_tag_name(tag_str)
            else:
                element = self.driver.find_element_by_tag_name(tag_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Tag '{}'".format(tag_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Tag: '{}'".format(tag_str)
        else:
            print "Couldn't find element by Tag '{}'".format(tag_str)
            return 0
        return element

    def findElementByPartialText(self,text_str,element=0):
        if not self.validateLocator(text_str):
            print "Invalid Partial Text: {}".format(text_str)
            return 0
        print "Searching for element by Partial Text: '{}'".format(text_str)
        try:
            if element:
                element = element.find_element_by_partial_link_text(text_str)
            else:
                element = self.driver.find_element_by_partial_link_text(text_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Partial Text '{}'".format(text_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Partial Text: '{}'".format(text_str)
        else:
            print "Couldn't find element by Partial Text '{}'".format(text_str)
            return 0
        return element

    def findElementByLinkText(self,link_str,element=0):
        if not self.validateLocator(link_str):
            print "Invalid Link Text: {}".format(link_str)
            return 0
        print "Searching for element by Link Text: '{}'".format(link_str)
        try:
            if element:
                element = element.find_element_by_link_text(link_str)
            else:
                element = self.driver.find_element_by_link_text(link_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Link Text '{}'".format(link_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Link Text: '{}'".format(link_str)
        else:
            print "Couldn't find element by Link Text '{}'".format(link_str)
            return 0
        return element

    def findElementByClass(self,class_str,element=0):
        if not self.validateLocator(class_str):
            print "Invalid Classname: {}".format(class_str)
            return 0
        print "Searching for element by Classname: '{}'".format(class_str)
        try:
            if element:
                element = element.find_element_by_class_name(class_str)
            else:
                element = self.driver.find_element_by_class_name(class_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Classname '{}'".format(class_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Classname: '{}'".format(class_str)
        else:
            print "Couldn't find element by Classname '{}'".format(class_str)
            return 0
        return element

    def findElementByXPath(self,xpath_str,element=0):
        if not self.validateLocator(xpath_str):
            print "Invalid Xpath: {}".format(xpath_str)
            return 0
        print "Searching for element by Xpath: '{}'".format(xpath_str)
        try:
            if element:
                element = element.find_element_by_xpath(xpath_str)
            else:
                element = self.driver.find_element_by_xpath(xpath_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by Xpath '{}'".format(xpath_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with Xpath: '{}'".format(xpath_str)
        else:
            print "Couldn't find element by Xpath '{}'".format(xpath_str)
            return 0
        return element

    def findElementByCSS(self,css_str,element=0):
        if not self.validateLocator(css_str):
            print "Invalid CSS Selector: {}".format(css_str)
            return 0
        print "Searching for element by CSS Selector: '{}'".format(css_str)
        try:
            if element:
                element = element.find_element_by_css_selector(css_str)
            else:
                element = self.driver.find_element_by_css_selector(css_str)
        except NoSuchElementException:
            print "NoSuchElementException: Couldn't find element by CSS Selector '{}'".format(css_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if isinstance(element, WebElement):
            self.selectedElement = element
            print "Found element with CSS Selector: '{}'".format(css_str)
        else:
            print "Couldn't find element by CSS Selector '{}'".format(css_str)
            return 0
        return element

    ##### Locating Multiple Elements #####

    def findElementsByName(self,name_str,element=0):
        if not self.validateLocator(name_str):
            print "Invalid Name: {}".format(name_str)
            return 0
        print "Searching for elements by Name: '{}'".format(name_str)
        try:
            if element:
                elements = element.find_elements_by_name(name_str)
            else:
                elements = self.driver.find_elements_by_name(name_str)
        except NoSuchElementException:
            print "Couldn't find any element by Name '{}'".format(name_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by Name '{}'".format(name_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by Name: '{}'".format(len(elements),name_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by Name '{}'".format(name_str)
            return 0
        return elements

    def findElementsByID(self,id_str,element=0):
        if not self.validateLocator(id_str):
            print "Invalid ID: {}".format(id_str)
            return 0
        print "Searching for elements by ID: '{}'".format(id_str)
        try:
            if element:
                elements = element.find_elements_by_id(id_str)
            else:
                elements = self.driver.find_elements_by_id(id_str)
        except NoSuchElementException:
            print "Couldn't find any element by ID '{}'".format(id_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by ID '{}'".format(id_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by ID: '{}'".format(len(elements),id_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by ID '{}'".format(id_str)
            return 0
        return elements

    def findElementsByTag(self,tag_str,element=0):
        if not self.validateLocator(tag_str):
            print "Invalid Tag: {}".format(tag_str)
            return 0
        print "Searching for elements by Tag: '{}'".format(tag_str)
        try:
            if element:
                elements = element.find_elements_by_tag_name(tag_str)
            else:
                elements = self.driver.find_elements_by_tag_name(tag_str)
        except NoSuchElementException:
            print "Couldn't find any element by Tag '{}'".format(tag_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by Tag '{}'".format(tag_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by Tag: '{}'".format(len(elements),tag_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by Tag '{}'".format(tag_str)
            return 0
        return elements

    def findElementsByPartialText(self,text_str,element=0):
        if not self.validateLocator(text_str):
            print "Invalid Partial Text: {}".format(text_str)
            return 0
        print "Searching for elements by Partial Text: '{}'".format(text_str)
        try:
            if element:
                elements = element.find_elements_by_partial_link_text(text_str)
            else:
                elements = self.driver.find_elements_by_partial_link_text(text_str)
        except NoSuchElementException:
            print "Couldn't find any element by Partial Text '{}'".format(text_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by Partial Text '{}'".format(text_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by Partial Text: '{}'".format(len(elements),text_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by Partial Text '{}'".format(text_str)
            return 0
        return elements

    def findElementsByLinkText(self,link_str,element=0):
        if not self.validateLocator(link_str):
            print "Invalid Link Text: {}".format(link_str)
            return 0
        print "Searching for elements by Link Text: '{}'".format(link_str)
        try:
            if element:
                elements = element.find_elements_by_link_text(link_str)
            else:
                elements = self.driver.find_elements_by_link_text(link_str)
        except NoSuchElementException:
            print "Couldn't find any element by Link Text '{}'".format(link_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by Link Text '{}'".format(link_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by Link Text: '{}'".format(len(elements),link_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by Link Text '{}'".format(link_str)
            return 0
        return elements

    def findElementsByClass(self,class_str,element=0):
        if not self.validateLocator(class_str):
            print "Invalid Classname: {}".format(class_str)
            return 0
        print "Searching for elements by Classname: '{}'".format(class_str)
        try:
            if element:
                elements = element.find_elements_by_class_name(class_str)
            else:
                elements = self.driver.find_elements_by_class_name(class_str)
        except NoSuchElementException:
            print "Couldn't find any element by Classname '{}'".format(class_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by Classname '{}'".format(class_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by Classname: '{}'".format(len(elements),class_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by Classname '{}'".format(class_str)
            return 0
        return elements

    def findElementsByXPath(self,xpath_str,element=0):
        if not self.validateLocator(xpath_str):
            print "Invalid XPath: {}".format(xpath_str)
            return 0
        print "Searching for elements by XPath: '{}'".format(xpath_str)
        try:
            if element:
                elements = element.find_elements_by_xpath(xpath_str)
            else:
                elements = self.driver.find_elements_by_xpath(xpath_str)
        except NoSuchElementException:
            print "Couldn't find any element by XPath '{}'".format(xpath_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by XPath '{}'".format(xpath_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by XPath: '{}'".format(len(elements),xpath_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by XPath '{}'".format(xpath_str)
            return 0
        return elements

    def findElementsByCSS(self,css_str,element=0):
        if not self.validateLocator(css_str):
            print "Invalid CSS Selector: {}".format(css_str)
            return 0
        print "Searching for elements by CSS Selector: '{}'".format(css_str)
        try:
            if element:
                elements = element.find_elements_by_css_selector(css_str)
            else:
                elements = self.driver.find_elements_by_css_selector(css_str)
        except NoSuchElementException:
            print "Couldn't find any element by CSS Selector '{}'".format(css_str)
            return 0
        except TimeoutException:
            print "TimeoutException: Can't determine loading status. Taking too long. " \
                  "Check your internet connection and try again"
            return 0
        if elements and len(elements) == 0:
            print "Couldn't find any element by CSS Selector '{}'".format(css_str)
            return 0
        elif len(elements) > 0:
            self.elements = elements
            print "Found {} elements by CSS Selector: '{}'".format(len(elements),css_str)
            self.selectedElement = self.elements[0]
        else:
            print "Couldn't find any element by CSS Selector '{}'".format(css_str)
            return 0
        return elements


    ##### Wrapper Functions #####

    def validateLocator(self, locator):
        if not locator:
            print "Locator is NULL"
            return 0
        if not isinstance(locator,str):
            print "Locator is not type str"
            return 0
        if locator == "" or locator == "\n" or locator == " " or locator.__contains__("\n") or len(locator) < 1:
            print "Locator is Invalid"
            return 0
        return 1

    def selectElement(self,element):
        if isinstance(element,WebElement):
            self.selectedElement = element
        elif isinstance(element,int):
            if self.elements == None or len(self.elements) == 0:
                print "Elements is empty"
                return 1
            else:
                index = element
                if index > len(self.elements)-1 or index < 0:
                    print "Invalid index to select element"
                    return 1
                self.selectedElement = self.elements[index]
        else:
            print "Error: Not element selected"
            return 1
        return 0

    def findElementLink(self,element):
        if element == 0 or not isinstance(element,WebElement):
            print "Element input argument is empty or is not Element type"
            return 0
        element_link = self.findElementByTag("a",element)
        if element_link == 0 or not isinstance(element_link,WebElement):
            print "The input element does not contain link address"
            return 0
        self.selectedElement = element_link
        return element_link

    def findSubElement(self,element,id=None,name=None,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None):
        err = self.selectElement(element)
        if err:
            return 0
        subelement = None
        if id:
            valid = self.validateLocator(id)
            if not valid:
                return
            subelement = self.findElementByID(id,element)
        if name:
            valid = self.validateLocator(name)
            if not valid:
                return
            subelement = self.findElementByName(name,element)
        if classname:
            valid = self.validateLocator(classname)
            if not valid:
                return
            subelement = self.findElementByClass(classname,element)
        if xpath:
            valid = self.validateLocator(xpath)
            if not valid:
                return
            subelement = self.findElementByXPath(xpath,element)
        if tag:
            valid = self.validateLocator(tag)
            if not valid:
                return
            subelement = self.findElementByTag(tag,element)
        if css:
            valid = self.validateLocator(css)
            if not valid:
                return
            subelement = self.findElementByCSS(css,element)
        if linktext:
            valid = self.validateLocator(linktext)
            if not valid:
                return
            subelement = self.findElementByLinkText(linktext,element)
        if partialtext:
            valid = self.validateLocator(partialtext)
            if not valid:
                return
            subelement = self.findElementByPartialText(partialtext,element)
        err = self.selectElement(subelement)
        if err:
            print "No Locator input argument passed to find sub-element"
            return 0
        else: return subelement

    def findElement(self,element=None,id=None,name=None,classname=None,xpath=None,tag=None,css=None,linktext=None,partialtext=None):
        # Find Element
        if not element:
            if id:
                valid = self.validateLocator(id)
                if not valid:
                    return
                element = self.findElementByID(id)
            if name:
                valid = self.validateLocator(name)
                if not valid:
                    return
                element = self.findElementByName(name)
            if classname:
                valid = self.validateLocator(classname)
                if not valid:
                    return
                element = self.findElementByClass(classname)
            if xpath:
                valid = self.validateLocator(xpath)
                if not valid:
                    return
                element = self.findElementByXPath(xpath)
            if tag:
                valid = self.validateLocator(tag)
                if not valid:
                    return
                element = self.findElementByTag(tag)
            if css:
                valid = self.validateLocator(css)
                if not valid:
                    return
                element = self.findElementByCSS(css)
            if linktext:
                valid = self.validateLocator(linktext)
                if not valid:
                    return
                element = self.findElementByLinkText(linktext)
            if partialtext:
                valid = self.validateLocator(partialtext)
                if not valid:
                    return
                element = self.findElementByPartialText(partialtext)
            err = self.selectElement(element)
            if err:
                print "No input argument to find element"
                return 0
            else: return element
        else:
            # Find Sub-Element
            if isinstance(element,WebElement):
                subelement = self.findSubElement(element=element,id=id,name=name,classname=classname,xpath=xpath,tag=tag,css=css,linktext=linktext,partialtext=partialtext)
                if subelement == None or subelement == 0 or not isinstance(subelement, WebElement):
                    print "Couldn't find Subelement of element {}".format(element)
                found = self.selectElement(subelement)
                if not found:
                    return
                else: return subelement
            # Find Sub-Element from List of Element by its locator
            elif isinstance(element,list):
                del self.elements[:]
                del self.elements
                self.elements = element
                for temp_element in self.elements:
                    if classname:
                        class_attr = temp_element.get_attribute("class")
                        if class_attr == classname:
                            self.selectElement(temp_element)
                            return temp_element
                    if name:
                        name_attr = temp_element.get_attribute("name")
                        if name_attr == name:
                            self.selectElement(temp_element)
                            return temp_element
                    if id:
                        id_attr = temp_element.get_attribute("id")
                        if id_attr == id:
                            self.selectElement(temp_element)
                            return temp_element
                    if tag:
                        tag_attr = temp_element.tag_name
                        if tag_attr == tag:
                            self.selectElement(temp_element)
                            return temp_element
                    if linktext:
                        linktext_attr = temp_element.text
                        if linktext_attr == linktext:
                            self.selectElement(temp_element)
                            return temp_element
                    if partialtext:
                        linktext_attr = temp_element.text
                        if partialtext in linktext_attr:
                            self.selectElement(temp_element)
                            return temp_element
                print "Couldn't find particular element from the list by given its locator"
                return 0
            else: return 0

    def findParentElement(self,element=0):
        if element:
            if isinstance(element,WebElement):
                self.selectElement(element)
            else:
                return 0
        if not isinstance(self.selectedElement,WebElement):
            return 0
        try:
            element = self.selectedElement.find_element_by_xpath('..')
        except NoSuchElementException:
            print "Element does not have parent element"
            return 0
        if element == 0 or element == None or not isinstance(element,WebElement):
            return 0
        else:
            self.selectElement(element)
            return self.selectedElement

    def findBodyElement(self):
        element = self.findElementByTag("body")
        if element == 0 or element == None:
            return 0
        else:
            self.selectElement(element)
