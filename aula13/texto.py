# INSTITUTO TECNOLOGICO DE AERONAUTICA
# CES-22: Programação Orientada a Objetos
# Prof. Dr. Edgar Yano
# Aluno: Bruno Doria
# 1 semestre 2018

# Exercício: identifique no projeto do grupo, situações onde os
# principios SOLID poderiam ser (ou foram) aplicados.

# Os princípios SOLID são conceitos, de Design Patterns em Programação Orientada a
# Objetos, que contribuem para facilidade de manutenção de código, facilidade de alterações,
# facilidade na correção de erros e escalabilidade da aplicação.
# Tendo em vista o projeto "Doctor Planning", pode-se observar a seguinte correspondência:
#
# S -> Single Responsablity: por exemplo a classe de eventos somente é modificada na sua criação
# (razão para modificação) pelo usuário; a classe de usuário paciente também é um outro possível exemplo
# pois sua responsabilidade se restringe a instanciar novos eventos.
#
# O -> Open Closed Design: por exemplo a classe relacionada a um evento marcado, seus campos são preenchidos
# apenas uma única vez pela interação do usuário, posteriormente a informação só é consultada e verificada para exibição
# de modo que não ocorrem modificações, apesar de serem utilizadas na exibição do calendário.
#
# L -> Liskov Substitution: poderiam ter sido considerados diversos tipos de eventos para agendamento
# (no caso, só houve a possibilidade de marcar uma consulta); por exemplo, poderia-se incluir eventos
# que se repetem automaticamente toda semana ou eventos com prioridade especial; para implementação
# dessas possibilidades poderiam ser consideradas extensões da classe original de evento com adição de
# funcionalidade ou característica particular, ou seja seguindo o princípio de aumentar a funcionalidade
# em relação à superclasse.
#
# I -> Interface Segregation: a ideia do projeto compreende basicamente dois tipos de usuários: pacientes e
# administradores da clínica; poderiam ter sido associadas maiores funcionalidades para o administrador, com
# métodos para o admin e métodos para o paciente tem-se aplicação do princípio, pois além dos diferentes templates
# associados a cada tipo, teríamos diferentes responsabilidades.
#
# D -> Dependency Inversion: se considerarmos a possibilidade de diferentes exibições de calendário, por exemplo,
# um calendário diário, semanal ou mensal a marcação de eventos deve ser análoga para o usuário, mas talvez sejam
# necessárias adaptações na implementação ou verificação dos objetos instanciados , desse modo tem-se os detalhes
# dependendo da abstração (agendamento de evento deve ser o mesmo).
#
