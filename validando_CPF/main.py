import design
import tratamento

def main():
    design.titulo('VALIDANDO UM CPF')
    CPF = str(input('Digite o CPF: ')).strip()
    CPF_1 = tratamento.validacao_CPF(CPF)    
    print(f'O CPF {CPF_1} está validado!') 
    

if __name__ == "__main__":
    main()