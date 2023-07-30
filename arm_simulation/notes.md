repositorios para brazos roboticos

    https://github.com/ros-industrial/abb
    https://github.com/ros-industrial/kuka_experimental

Paso 1: Modificar el nombre del robot en el launch de basic_simulation Linea 2

Paso 2: Modifica el archivo xacro en la segunda parte de la linea 2

-----------------------------------------------------------
Para moveit
    sudo apt install ros-noetic-moveit

para ejecutarlo 
    roslaunch moveit_setup_assistant setup_assistant.launch

para modificar una configuracion ya hecha
    roslaunch irb4400_moveit setup_assistant.launch

ejecutar moveit
    roslaunch irb6640_moveit_package demo.launch 

repositorio tutorial
    https://github.com/WilberRojas/ROS-smartPAD/tree/kcp-v4


para programar movimientos
    abrir rviz con moviet
    ejecutar la estructura
    ejecutar la secuencia


# ROS SmartPAD v4
Tutorial: </br>
https://youtu.be/6XYw795jLpA

Paso 1: mover la carpeta /kcp a /src
Paso 2: compilar ROS
Paso 3: iniciar rviz
Paso 4: ejecutar roslaunch kcp smartpad.launch group:=irb6644
Paso 5: cd src/kcp/scripts/
    chmod +x *.py
    cd config_rviz/
    chmod +x *.py
    cd 0.\ next\ updates/
    chmod +x *.py

