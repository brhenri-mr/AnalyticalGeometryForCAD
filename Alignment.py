import numpy as np
from sympy import symbols, Eq, solve

def rotate_vector(vector, angle):
    '''
    Rotationa o vector no sentindo anti horario
    vector: vetor a ser rotacionado
    angle: Angulo em radianos
    return: vector
    '''
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                               [np.sin(angle), np.cos(angle)]])
    rotated_vector = np.dot(rotation_matrix, vector)

    return rotated_vector

def parametric_equation_rotated_line(original_direction_vector, rotation_angle):
    rotated_direction_vector = rotate_vector(original_direction_vector, rotation_angle)
    x_parametric = rotated_direction_vector[0]
    y_parametric = rotated_direction_vector[1] 
    return x_parametric, y_parametric

def vetor_ortogonal(vetor):
    '''
    Retorna o vetor ortogonal ao vector de input
    vector: vetor
    return: vector
    
    '''
    vetor_ortogonal = np.array([-vetor[1], vetor[0]])

    return vetor_ortogonal

def interseccao(ponto1:list,ponto2:list,grad_anterior:list) ->list:
    '''
    Funcao para calculo do ponto de intersecao entre o gradiente ortogonal a tangente
    e a mediatriz da corda dos pontos
    ponto1: ponto base da corda
    ponto2: ponto final da corda
    grad_anterior: vetor direcao da tagente do ponto base (vindo do calculo anterior)
    return: vec,raio, comprimento,angulo
    '''

    '''
    O calculo é feito com o as retas parametricas da mediatriz da corda base e com a reta ortogonal a tangente do ponto inicial
    A ideia foi q eu sei a primeira direcao da tangente, logo sempre obter a proxima utilizando o centro (intersecao) e o ponto final
    O calculo do raio foi feito com a distancia intersecao e o ponto inicial
    
    '''

    # Dados
    original_direction_vector = np.array([1, 0])  # Vetor Base
    x1,y1 = ponto1[0], ponto1[1] # ponto inicial 
    xf,yf = ponto2[0], ponto2[1]# ponto final 
    x2,y2 = (xf+x1)/2,(yf+y1)/2 # Ponto medio


    ang_alinhamento_atual = np.arctan2((yf-y1),(xf-x1))

    
    test = ang_alinhamento_atual+np.pi/2


    x_rotated_1, y_rotated_1 = vetor_ortogonal(grad_anterior)

    x_rotated_2, y_rotated_2 = parametric_equation_rotated_line(original_direction_vector, test)


    t, s,= symbols('t s')

    # Equações paramétricas das retas originais
    eq1 = Eq(x1 + t * x_rotated_1, x2 + s * x_rotated_2)
    eq2 = Eq(y1 + t * y_rotated_1, y2 + s * y_rotated_2)

    #Calculo Do ponto de intersecao
    solution = solve((eq1, eq2), (t, s))
    try:
        intersection_point = [x1 + solution[t] * x_rotated_1, y1 + solution[t] * y_rotated_1]

        #print(intersection_point)
        Comprimento = ((xf-x1)**2+(yf-y1)**2)**(0.5)
        raio = ((intersection_point[0]-x1)**2+(intersection_point[1]-y1)**2)**(0.5)
        vec = vetor_ortogonal([intersection_point[0]-xf,intersection_point[1]-yf])
        #print(f'Raio:{raio}')
        #print(f'Comprimento:{((xf-x1)**2+(yf-y1)**2)**(0.5)}')




        return vec,raio,Comprimento,Comprimento/raio*0.5
    
    except:
        print('Erro')

        return 1

if __name__ == '__main__':
    interseccao([0 ,0],[12353.8153,10656.5864],0)