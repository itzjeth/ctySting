function submitPoll(){
    document.getElementById("sendInput").disabled = true;
    setTimeout(function() {
        document.getElementById("sendInput").disabled = false;
    }, 20000);
    
} 

document.getElementById("sendInput").addEventListener("click", submitPoll);