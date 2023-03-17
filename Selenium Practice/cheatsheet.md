### Selenium WebDriver

---

## What is webDriver?

->WebDriver is one of the component of selenium <br/>
-> WebDriver is module

## Locators

->id<br/>
->name<br/>
->LinkText / Partial LinkText<br/>
->class name<br/>
->tag name<br/>

## Customized Locators

->CSS Selector<br/>
---1. tag and id<br/>
---2. tag and class<br/>
---3. tag and attribute<br/>
---4. tag and class attribute<br/>

->XPath<br/>
---1. Absolute/ Full Xpath<br/>
---2. Relative/ Xpath<br/>

->Reason to prefer relative XPath<br/>
---1. if developer introduced new element then absolute xpath will be broken.<br/>
---2. if developer changed the location then absolute xpath will be broken.<br/>

-> Which XPath is preferd?<br/>
--- Relative. Absolute xpath is unstable.<br/>

### XPath Options<br/>

---1. and <br>
---2. or <br>
---3. contains() <br>
---4. starts-with() <br>
---5. text() <br>

### XPath Axes<br/>

---1. self <br>
---2. parent <br>
---3. child <br>
---4. ancestor <br>
---5. descendant(grand-child) <br>
---6. following (nodes above self)<br>
---7. following-sibling(nodes after following in right side)<br>
---4. preceding(nodes after following in left side) <br>
---5. preceding-sibling (nodes after preceding nodes)<br>

### WebDriver Commands

---1. get commands
---2. conditional commands
---3. broswer commands
---4. navigational commands
---5. wait commands

### Application Commands

---

--- get() #opening the application url
---1. title # capture the title of current page
---2. curent_url # capture the url of current page
---3. page_source # capture the source code of current page

### Conditionals Commands

---

1. is_displayed()
2. is_enabled()
3. is_selected()

### Broswer Commands

---

1. close()
2. quit()

### Navigational Commands

1. back()
2. forward()
3. refresh()

### Wait Commands

1. implicit wait
2. explicit wait

### Links

1. External Links
2. Internal Links
3. Broken Links

### Alerts

a=driver.switch_to.alert
print(a.text)
driver.accept()
driver.dismiss()

### Authentication Alerts

### Frames

a.switch_to.frame(name of the frame)
a.switch_to.frame(id of the frame)
a.switch_to.frame(webelement)
a.switch_to.frame(0)

# broswer windows

a.switch_to.window(windowId)

current_window_handle #return windowID of single broswer windows

window_handle # return windowIds of multiple browser windows
