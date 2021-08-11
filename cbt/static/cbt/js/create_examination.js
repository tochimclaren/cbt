"use strict"
const examinationForm =  document.querySelector("#ExaminationForm");
const subjectForm = document.querySelector("#subjectForm");
const exams = document.querySelectorAll(".exam");

function getExams(){
    exams.forEach(exam=>{
        exam.addEventListener("click", e=>{
            e.preventDefault();
            console.log(e.target.dataset.id)
        });
    });
}

getExams()

function createExamination(examinationForm){
    examinationForm.addEventListener("submit", e=>{
        e.preventDefault();
        const formData = new FormData(examinationForm);

        fetch("/create_examination/", {
            body: formData,
            method: "post"    
        })
        .then(response => response.json())
        .then(result => {console.log(result)})
        .catch(error =>{console.log(error)})
    })
}

createExamination(examinationForm)
