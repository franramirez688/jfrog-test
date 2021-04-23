import logo from './logo.svg';
import './App.css';

import Contacts from './components/contacts'
import React, { Component } from 'react';

    class App extends Component {
      state = {
        contacts: []
      }

      componentDidMount() {
        fetch(process.env.REACT_APP_WEB_API + '/contacts')
        .then(res => res.json())
        .then((data) => {
          this.setState({ contacts: data })
        })
        .catch(console.log)
      }

      render() {
        return (
          <Contacts contacts={this.state.contacts} />
        )
      }
    }

export default App;
