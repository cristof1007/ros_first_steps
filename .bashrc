# Mis Alias:
alias asd='source devel/setup.bash'
alias asd2='source install/setup.bash'
alias qwe='catkin_make'
alias qwer='catkin build'
alias qwe2='colcon build'
alias qwe2_pkg='colcon build --packages-select'

alias noetic='source /opt/ros/noetic/setup.bash'
alias galactic='source /opt/ros/galactic/setup.bash'
alias rqt_gui='rosrun rqt_gui rqt_gui'
alias moveit='roslaunch moveit_setup_assistant setup_assistant.launch'
alias husarnet_on='export ROS_IPV6=on && export ROS_HOSTNAME=ubuntu && export ROS_MASTER_URI=http://master:11311 && husarnet start'
alias husarnet_off='husarnet stop && export ROS_IPV6=off && export ROS_HOSTNAME=ubuntu.local && export ROS_MASTER_URI=http://ubuntu.local:11311'

alias coppelia='cd ~/Documents/CoppeliaSim && ./coppeliaSim.sh'
alias xampp='sudo /opt/lampp/manager-linux-x64.run'

alias update='sudo apt-get update'
alias upgrade='sudo apt-get upgrade'
alias python='python3'
alias sbash='source ~/.bashrc'

alias mp4_to_mp3='ffmpeg -i input.mp4 -vn -f mp3 -ab 192k output.mp3'
alias deldocker='function _deldocker(){ docker stop $1 && docker rm $1; };_deldocker'

supergit() {
  if [[ $1 == "update" ]]; then
    if [[ -z $2 ]]; then
      echo "Por favor, proporciona un mensaje de commit."
    else
      git status
      git add .
      git commit -m "$2"
      git push 
    fi
  elif [[ $1 == "server2" ]]; then
    echo "nothing here :)"
  else
    echo "update: status, add ., commit, push"
  fi
}