#!/usr/bin/python
# -*- coding: utf-8 -*-
# Data: 30/08/2025 - github.com/phlimma
# Script para retirar a senha de todos os PDFs localizados na pasta da rotina e subpastas.

import os
import sys
import subprocess

# --------- VERIFICAR/INSTALAR PyPDF2 ---------
try:
    import PyPDF2
except ImportError:
    print("Biblioteca PyPDF2 não encontrada. Instalando...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
    import PyPDF2


def encontrar_pdfs(diretorio):
    """Varre o diretório e subdiretórios recursivamente procurando PDFs"""
    arquivos_pdf = []
    for root, _, files in os.walk(diretorio):
        for file in files:
            if file.lower().endswith(".pdf"):
                arquivos_pdf.append(os.path.join(root, file))
    return arquivos_pdf


def remover_senha(pdf_path, senha):
    """Tenta remover a senha do PDF"""
    try:
        pdf = PyPDF2.PdfReader(open(pdf_path, "rb"))

        if pdf.is_encrypted:
            if pdf.decrypt(senha):
                pdf_writer = PyPDF2.PdfWriter()
                for page_num in range(len(pdf.pages)):
                    pdf_writer.add_page(pdf.pages[page_num])

                novo_pdf = os.path.splitext(pdf_path)[0] + "_semsenha.pdf"
                with open(novo_pdf, "wb") as output_pdf:
                    pdf_writer.write(output_pdf)

                print(f"[OK] Senha removida de '{os.path.basename(pdf_path)}'. Salvo como '{os.path.basename(novo_pdf)}'")
            else:
                print(f"[ERRO] Senha incorreta para '{os.path.basename(pdf_path)}'.")
        else:
            print(f"[INFO] '{os.path.basename(pdf_path)}' não está protegido por senha.")

    except Exception as e:
        print(f"[ERRO] Não foi possível processar '{pdf_path}': {e}")


if __name__ == "__main__":
    # Obtendo o diretório atual
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))

    print("\n Procurando arquivos PDF...\n")
    pdfs = encontrar_pdfs(diretorio_atual)

    if not pdfs:
        print("Nenhum PDF encontrado.")
    else:
        senha = input("Digite a senha para tentar desbloquear os PDFs: ")
        print("\n--- Iniciando processamento ---\n")
        for pdf in pdfs:
            remover_senha(pdf, senha)

    input("\nRotina finalizada. Pressione ENTER para encerrar...")
