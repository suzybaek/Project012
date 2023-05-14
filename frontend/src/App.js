import React from 'react';
import { Route, Switch } from 'react-router-dom';

import MainPage from './pages/MainPage';
import TestPage from './pages/TestPage';
import TestCompletedPage from './pages/TestCompletedPage';
import MbtiCharacterPage from './pages/MbtiCharacterPage';
import MbtiCharacterMovieListPage from './pages/MbtiCharacterMovieListPage';
import MbtiCompatiblePage from './pages/MbtiCompatiblePage';
import MbtiCompatibleMovieListPage from './pages/MbtiCompatibleMovieListPage';
import MbtiTop10Page from './pages/MbtiTop10Page';


function App() {
  return (
    <div className="App">
      <Switch>
        <Route exact path="/" component={ MainPage } />
        <Route path="/TestPage" component={ TestPage } />
        <Route path="/TestCompletedPage" component={ TestCompletedPage } />
        <Route path="/MbtiCharacterPage" component={ MbtiCharacterPage } />
        <Route path="/MbtiCharacterMovieListPage" component={ MbtiCharacterMovieListPage } />
        <Route path="/MbtiCompatiblePage" component={ MbtiCompatiblePage } />
        <Route path="/MbtiCompatibleMovieListPage" component={ MbtiCompatibleMovieListPage } />
        <Route path="/MbtiTop10Page" component={ MbtiTop10Page } />
      </Switch>
    </div>
  );
}

export default App;
