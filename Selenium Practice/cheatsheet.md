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
