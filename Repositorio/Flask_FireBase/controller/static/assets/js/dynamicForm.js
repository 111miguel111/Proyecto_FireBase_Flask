function createInputs() {
    var numberOfInputs = parseInt(document.getElementById("materia").value);
    var form = document.getElementById("dynamicForm");


    boton = document.getElementById("env")
    form.removeChild(boton);
    // Clear existing inputs
    for (var i = 0; i < 5; i++) {
        espacio = document.getElementById("spc" + (i + 1));
        label = document.getElementById("label" + (i + 1));
        input = document.getElementById("slot" + (i + 1));

        if (form.contains(espacio)) {
            form.removeChild(espacio);
        }

        if (form.contains(input)) {
            form.removeChild(input);

        }

        if (form.contains(label)) {
            form.removeChild(label);
        }
    }

    // Create new inputs
    for (var i = 0; i < numberOfInputs; i++) {
        var label = document.createElement("label");
        label.for = "slot" + (i + 1);
        label.textContent = "slot de materia " + (i + 1) + ":";
        label.id = "label" + (i + 1);
        form.appendChild(label);

        var input = document.createElement("input");
        input.type = "text";
        input.name = "slot" + (i + 1); // Setting unique name for each input
        input.id = "slot" + (i + 1);
        form.appendChild(input);

        var espacio = document.createElement("br")
        espacio.id = "spc" + (i + 1);
        form.appendChild(espacio); // Line break for spacing
    }

    // Add submit button
    var submitButton = document.createElement("input");
    submitButton.type = "submit";
    submitButton.value = "Enviar";
    submitButton.id = "env";
    form.appendChild(submitButton);
}