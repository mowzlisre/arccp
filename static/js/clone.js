function cloneFunction() {
    obj = $("#question-area").children().last().clone()
    $("#question-area").append(obj)
    last = $("#question-area").children().last()
    id = parseInt(last.attr("id").slice(14)) + 1
    last.attr("id", 'question-card-' + id)


    radio = document.getElementById("answer-" + (id - 1)).value
    console.log(radio);

    document.getElementById("counter").value = id
    $(last).children("#question-id-" + (id - 1)).attr("id", 'question-id-' + id)
    document.getElementById("question-id-" + id).innerHTML = "Question " + id + ":"


    $(last).children("#question-" + (id - 1)).attr("id", 'question-' + id)
    $(last).children("#question-" + (id)).attr("name", 'question-' + id)
    $(last).children("#question-" + (id)).val('')
    $(last).children("#option").children("#answer-" + (id - 1)).attr("id", 'answer-' + id)
    $(last).children("#option").children("#answer-" + (id)).attr("name", 'answer-' + id)
    $(last).children("#option").children("#answer-" + (id)).prop("checked", false)
    $(last).children("#question-" + (id - 1) + "-1").attr("id", 'question-' + id + "-1")
    $(last).children("#question-" + (id - 1) + "-2").attr("id", 'question-' + id + "-2")
    $(last).children("#question-" + (id - 1) + "-3").attr("id", 'question-' + id + "-3")
    $(last).children("#question-" + (id - 1) + "-4").attr("id", 'question-' + id + "-4")
    $(last).children("#question-" + (id) + "-1").attr("name", 'question-' + id + "-1")
    $(last).children("#question-" + (id) + "-2").attr("name", 'question-' + id + "-2")
    $(last).children("#question-" + (id) + "-3").attr("name", 'question-' + id + "-3")
    $(last).children("#question-" + (id) + "-4").attr("name", 'question-' + id + "-4")
    $(last).children("#question-" + (id) + "-1").val('')
    $(last).children("#question-" + (id) + "-2").val('')
    $(last).children("#question-" + (id) + "-3").val('')
    $(last).children("#question-" + (id) + "-4").val('')
}

function deleteLast() {
    obj = $(this).parent().parent()
    if ($("#question-area").children().length > 1) {
        obj.remove()
        document.getElementById("counter").value -= 1
    }
}