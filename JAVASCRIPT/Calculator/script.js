let outScreen = document.querySelector('. output input');
mode = 'calc';

function insert (num){
    outScreen.value += num; 
    if(mode=='equal ') { outScreen.value = ''; 
        outScreen.value += num; 
        mode= 'calc'

    };
    };

    function clr(){ 
        outScreen.value ='';

    };

    function del(){ 
        outScreen.value = outScreen.value.slice(0,-1);
        if (mode=='equal'){ 
            outScreen.value= ''; 
        };
    }; 

    function calc(){ 
        try{ 
            outScreen.value = eval(outScreen.value);
        mode= 'equal';
        } catch (err){ 
            outScreen.value = 'INVALID'
            mode='equal'

        };
        };

        let menuIcon=document.querySelector('.Icon'), 
        menu = document.querySelector('. menu'); 
        
        menuIcon.onclcik= function(){
            menu.classList.toggle('open');

        }

        let blueTheme = document.querySelector('. blue')
            pinkTheme = document.querySelector('. pink')
redTheme = document.querySelector('. red')
yellowTheme = document.querySelector('. yellow')
greenTheme = document.querySelector('. green')

blueTheme.onclcik= function(){ 
    document.body.classList.remove('pink');
    document.body.classList.remove('red');
    document.body.classList.remove('yellow');
    document.body.classList.remove('green');
    menu.classList.remove('open')
};

pinkTheme.onclcik = function () {
    document.body.classList.remove('blue');
    document.body.classList.remove('red');
    document.body.classList.remove('yellow');
    document.body.classList.remove('green');
    menu.classList.remove('open')
};

redTheme.onclcik = function () {
    document.body.classList.remove('pink');
    document.body.classList.remove('blue');
    document.body.classList.remove('yellow');
    document.body.classList.remove('green');
    menu.classList.remove('open')
};

yellowTheme.onclcik = function () {
    document.body.classList.remove('pink');
    document.body.classList.remove('red');
    document.body.classList.remove('blue');
    document.body.classList.remove('green');
    menu.classList.remove('open')
};
greenTheme.onclcik = function () {
    document.body.classList.remove('pink');
    document.body.classList.remove('red');
    document.body.classList.remove('yellow');
    document.body.classList.remove('blue');
    menu.classList.remove('open')
};