import React, {PropsWithRef, SyntheticEvent, useEffect, useState} from 'react';
import {Redirect} from "react-router";
import Wrapper from "./Wrapper";
import {Produto} from "../interfaces/produto";

const AtualizarProduto = (props: PropsWithRef<any>) => {
    const [titulo, setTitulo] = useState('')
    const [imagem, setImagem] = useState('')
    const [redirect, setRedirect] = useState(false)

    useEffect(() => {
        (
            async () => {
                const response = await fetch(`http://localhost:8000/api/produtos/${props.match.params.id}`)
                const produto: Produto = await response.json()
                setTitulo(produto.titulo)
                setImagem(produto.imagem)
            }
        )()
    }, [])

    const submit =  async (e: SyntheticEvent) => {
        e.preventDefault()
        await fetch(`http://localhost:8000/api/produtos/${props.match.params.id}`, {
            method: 'PUT',
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
                           defaultValue={titulo}
                           onChange={e => setTitulo(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Imagem</label>
                    <input type="text" className="form-control" name="imagem"
                           defaultValue={imagem}
                           onChange={e => setImagem(e.target.value)}
                    />
                    <button className="btn btn-success mt-1">Salvar</button>
                </div>
            </form>
        </Wrapper>
    );
};

export default AtualizarProduto;