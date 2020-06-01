document.addEventListener('DOMContentLoaded', () => {

    document.querySelector('#submit').disabled = true;

    document.querySelector('#task').onkeyup = () => {
        if(document.querySelector('#task').value.lenght > 0){
            document.querySelector('#submit').disabled = false;
        }
        else{
            document.querySelector('#submit').disabled = false;
        }

    };
    
    document.querySelector('#new-task').onsubmit = () => {
        // create new li Element
    const li = document.createElement('li');
    li.innerHTML = document.querySelector('#task').value;

    // add li to the ul 
    document.querySelector('#tasks').append(li);

    document.querySelector('#task').value = '';
    document.querySelector('#submit').disabled = true;

    // stop reload page 
    return false;
    };
    
});