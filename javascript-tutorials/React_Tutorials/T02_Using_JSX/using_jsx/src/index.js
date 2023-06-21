import React from 'react'
import ReactDOM from 'react-dom/client'

const withJsx = <h1>I Love JSX!</h1>
const withoutJsx = React.createElement('h1', {}, 'I do not use JSX!')
const usingExpressions = <h1>React is {5 + 5} times better with JSX</h1>
const multiLineHtml = (
  //use brackets for multiline html
  <ul>
    <li>Apples</li>
    <li>Bananas</li>
    <li>Cherries</li>
  </ul>
)

const onlyOneTopLevelElement = (
  //HTML code can only have one top level element
  <div>
    <p>Paragraph one</p>
    <p>Paragraph two</p>
  </div>
)

const elementsMustBeClosed = (
  <div>
    <input type='text' />
    <hr />
  </div>
)

const classReservedUseClassName = <h2 className="myclass">Because JavaScript stole class</h2>;

const usingIfStatements = <h3>{Math.random < 10 ? "Hello" : "Goodbye"}</h3>;

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render([
  withJsx,
  withoutJsx,
  usingExpressions,
  multiLineHtml,
  onlyOneTopLevelElement,
  elementsMustBeClosed,
  classReservedUseClassName,
  usingIfStatements
])
