/**
 * Vishwakarma AI - Main JavaScript Controller
 * © 2025 Vishwakarma Industries
 */

$(document).ready(function () {

    eel.init()()
    
    // Profile Form Submission
    $("#profileForm").submit(function(e) {
        e.preventDefault();
        
        const name = $("#userName").val();
        const age = $("#userAge").val() || null;
        const preferences = {
            news: $("#prefNews").is(":checked"),
            weather: $("#prefWeather").is(":checked"),
            reminders: $("#prefReminders").is(":checked")
        };
        
        // Show loading state
        const submitBtn = $(this).find('button[type="submit"]');
        const originalText = submitBtn.html();
        submitBtn.html('<span>Creating Profile...</span><i class="bi bi-hourglass-split"></i>');
        submitBtn.prop('disabled', true);
        
        eel.createProfile(name, age, preferences)(function(response) {
            if (response.success) {
                console.log("Profile created successfully");
                // Show success message briefly
                submitBtn.html('<span>Success!</span><i class="bi bi-check-circle"></i>');
                setTimeout(function() {
                    submitBtn.html(originalText);
                    submitBtn.prop('disabled', false);
                }, 1000);
            } else {
                alert("Failed to create profile: " + response.error);
                submitBtn.html(originalText);
                submitBtn.prop('disabled', false);
            }
        });
    })

    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    // Siri configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.30",
        autostart: true
      });

    // Siri message animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    // mic button click event

    $("#MicBtn").click(function () { 
        eel.playAssistantSound()
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.allCommands()()
    });


    function doc_keyUp(e) {
        // this would test for whichever key is 40 (down arrow) and the ctrl key at the same time

        if (e.key === 'j' && e.metaKey) {
            eel.playAssistantSound()
            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands()()
        }
    }
    document.addEventListener('keyup', doc_keyUp, false);

    // to play assisatnt 
    function PlayAssistant(message) {

        if (message != "") {

            $("#Oval").attr("hidden", true);
            $("#SiriWave").attr("hidden", false);
            eel.allCommands(message);
            $("#chatbox").val("")
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);

        }

    }

    // toogle fucntion to hide and display mic and send button 
    function ShowHideButton(message) {
        if (message.length == 0) {
            $("#MicBtn").attr('hidden', false);
            $("#SendBtn").attr('hidden', true);
        }
        else {
            $("#MicBtn").attr('hidden', true);
            $("#SendBtn").attr('hidden', false);
        }
    }

    // key up event handler on text box
    $("#chatbox").keyup(function () {

        let message = $("#chatbox").val();
        ShowHideButton(message)
    
    });
    
    // send button event handler
    $("#SendBtn").click(function () {
    
        let message = $("#chatbox").val()
        PlayAssistant(message)
    
    });
    

    // enter press event handler on chat box
    $("#chatbox").keypress(function (e) {
        key = e.which;
        if (key == 13) {
            let message = $("#chatbox").val()
            PlayAssistant(message)
        }
    });




});