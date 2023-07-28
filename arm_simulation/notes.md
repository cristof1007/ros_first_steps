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

