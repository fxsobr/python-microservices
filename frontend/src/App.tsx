import React from 'react';
import './App.css';
import Produtos from "./admin/Produtos";
import {BrowserRouter, Route} from "react-router-dom";
import Main from "./main/Main";
import NovoProduto from "./admin/NovoProduto";
import AtualizarProduto from "./admin/AtualizarProduto";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Route path='/' exact component={Main}/>
                <Route path='/admin/produtos' exact component={Produtos}/>
                <Route path='/admin/produtos/novo' exact component={NovoProduto}/>
                <Route path='/admin/produtos/:id/atualizar' exact component={AtualizarProduto}/>
            </BrowserRouter>
        </div>
    );
}

export default App;
