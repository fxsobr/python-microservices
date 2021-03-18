import React, {useEffect, useState} from 'react';
import Wrapper from "./Wrapper";
import {Produto} from "../interfaces/produto";
import {Link} from "react-router-dom";

const Produtos = () => {
    const [produtos, setProdutos] = useState([]);

    useEffect(() => {
        (
            async () => {
                const response = await fetch('http://localhost:8000/api/produtos')
                const data = await response.json()

                setProdutos(data)
            }
        )();
    }, []);

    const remover = async (id: number) => {
        if (window.confirm('Você tem certeza que deseja remover esse produto?')) {
            await fetch(`http://localhost:8000/api/produtos/${id}`, {
                method: 'DELETE'
            })
            setProdutos(produtos.filter((p: Produto) => p.id !== id))
        }
    }

    return (
        <Wrapper>
            <div className="pt-3 pb-2 mb-3 border-bottom">
                <div className="btn-toolbar mb-2 mb-md-0">
                    <Link to='/admin/produtos/novo' className="btn btn-success btn-sm">Novo Produto</Link>
                </div>
            </div>
                <div className="table-responsive">
                    <table className="table table-striped table-sm">
                        <thead>
                        <tr>
                            <th>#</th>
                            <th>Imagem</th>
                            <th>Titulo</th>
                            <th>Curtidas</th>
                            <th>Ações</th>
                        </tr>
                        </thead>
                        <tbody>
                        {produtos.map(
                            (p: Produto) => {
                            return (
                                <tr key={p.id}>
                                    <td>{p.id}</td>
                                    <td><img src={p.imagem} height="180"/></td>
                                    <td>{p.titulo}</td>
                                    <td>{p.curtidas}</td>
                                    <td>
                                        <Link to={`/admin/produtos/${p.id}/atualizar`} className="btn btn-warning btn-sm mr-1">Atualizar</Link>
                                        <a href="#" className="btn btn-danger btn-sm"
                                           onClick={() => remover(p.id)}>Remover</a>
                                    </td>
                                </tr>
                            )
                        })}
                        </tbody>
                    </table>
                </div>
        </Wrapper>
    );
};

export default Produtos;