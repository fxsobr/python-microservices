import React, {SyntheticEvent, useState} from 'react';
import Wrapper from "./Wrapper";
import {Redirect} from "react-router";

const NovoProduto = () => {
    const [titulo, setTitulo] = useState('')
    const [imagem, setImagem] = useState('')
    const [redirect, setRedirect] = useState(false)

    const submit =  async (e: SyntheticEvent) => {
        e.preventDefault()
        await fetch('http://localhost:8000/api/produtos', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                titulo: titulo,
                imagem: imagem
            })
        })
        setRedirect(true)
    }

    if(redirect) {
        return <Redirect to='/admin/produtos' />
    }

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                   <label>Titulo</label>
                    <input type="text" className="form-control" name="titulo"
                        onChange={e => setTitulo(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Imagem</label>
                    <input type="text" className="form-control" name="imagem"
                        onChange={e => setImagem(e.target.value)}
                    />
                    <button className="btn btn-success mt-1">Salvar</button>
                </div>
            </form>
        </Wrapper>
    );
};

export default NovoProduto;