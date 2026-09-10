# Robot Control Lab

Ambiente didático de simulação para a disciplina de Modelagem e Controle de Robôs.

## Objetivo

Desenvolver uma plataforma baseada em ROS 2 e Gazebo para:

- validação de modelos cinemáticos;
- validação de modelos dinâmicos;
- implementação e teste de controladores;
- comparação de resultados MATLAB × Gazebo;
- aquisição e análise automática de dados.

## Plataformas

### Manipulador 2R
Ambiente de treinamento para aprendizagem da infraestrutura ROS 2/Gazebo.

### Universal Robots
Plataforma para os trabalhos avaliativos:

- UR3e;
- UR5e.

## Ambiente de desenvolvimento

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic
- ros2_control / gz_ros2_control

## Estrutura

- `ros2_ws/`: workspace ROS 2
- `config/`: configurações dos robôs e controladores
- `matlab/`: modelos e simulações MATLAB
- `experiments/`: definição dos experimentos
- `docs/`: documentação, laboratórios e slides
- `docker/`: ambiente reproduzível para os alunos
- `tests/`: testes automatizados
