# Databricks notebook source
import os
import random
import time

def construir_lista_estacoes_meteorologicas(file_path):
    with open(file_path, 'r', encoding='utf-8') as arquivo:
        return list(set(linha.split(';')[0] for linha in arquivo if '#' not in linha))
    
def converter_bytes(num):
    for unidade in ['B', 'KB', 'MB', 'GB']:
        if num < 1024:
            return f'{num:.2f} {unidade}'
        num /= 1024

def formatar_tempo_decorrido(segundos):
    minutos, segundos = divmod(segundos, 60)
    return f'{int(minutos)}m {int(segundos)}s' if minutos else f'{segundos:.2f}s'

def gerar_dados_teste(file_path, output_path, num_registros):
    inicio_tempo = time.time()
    nomes_estacoes = construir_lista_estacoes_meteorologicas(file_path)
    estacoes_10k_max = random.choices(nomes_estacoes, k=10_000)
    tamanho_lote = 10_000 # processamento em lotes

    print(f'Criando {output_path}...')

    try:
        with open(output_path, 'w', encoding='utf-8') as arquivo:
            for _ in range(num_registros // tamanho_lote):
                lote = random.choices(estacoes_10k_max, k=tamanho_lote)
                linhas = '\n'.join([f'{estacao};{random.uniform(-99.9, 99.9):.1f}' for estacao in lote])
                arquivo.write(linhas + '\n')
        
        tamanho_arquivo = os.path.getsize(output_path)
        print(f'Arquivo gerado: {output_path}')
        print(f'Tamanho final: {converter_bytes(tamanho_arquivo)}')
        print(f'Tempo decorrido: {formatar_tempo_decorrido(time.time() - inicio_tempo)}')
    except Exception as e:
        print('Erro ao gerar dados:', e)

if __name__ == '__main__':
    file_path = '/Volumes/workspace/default/etl_pipelines/amostra_44k.csv'
    output_path = '/Volumes/workspace/default/etl_pipelines/meducies_1bilhao.txt'
    num_registros = 1_000_000_000
    gerar_dados_teste(file_path, output_path, num_registros)




