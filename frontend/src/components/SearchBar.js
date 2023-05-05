import React from 'react';
import "../css_files/SearchBar.css"
function SearchBar(props) {
  return (
    <div className='search_container'>
        <div classname="search_input">
        <input type="tex" placeholder="Search..." onChange={props.handleChange}/>
        <button type="button" onClick={props.handleClick} className='search_button'>Search</button>
        </div>
    </div>
  );
}

export default SearchBar;
