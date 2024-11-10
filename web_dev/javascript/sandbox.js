function load_page_defaults(){
    let intro = document.getElementById("intro_header");
    intro.innerHTML = "JavaScript Sandbox V1";
    intro.style.textDecoration = "underline";

    let about_dev = document.getElementById("about_the_dev");

    developer = load_developer_profile();

    document.getElementById("dev_name").innerHTML = "<b>Name: </b>" + developer.fullName();
    document.getElementById("dev_title").innerHTML = "<b>Title: </b>" + developer.title;
    document.getElementById("dev_phone").innerHTML = "<b>Phone: </b>" + developer.phone;
    document.getElementById("dev_email").innerHTML = "<b>Email: </b>" + developer.email;
    document.getElementById("dev_website").innerHTML = "<b>Website: </b>" + developer.website;
    document.getElementById("dev_langs").innerHTML = "<b>Languages: </b><ul>" + developer.returnLangs() + "</ul>";
    document.getElementById("dev_knowledge").innerHTML = "<b>Knowledge: </b><ul>" + developer.returnKnowledge() + "</ul>";


}

function load_developer_profile(){
    const prog_developer = {
            fName: "Keith",
            lName: "Kornacki",
            title: "Software Engineer",
            dob: "04/14/1992",
            email: "Keith.Kornacki@outlook.com",
            phone: "(248) 497-6047",
            website: "www.about-the-dev.com",
            nativeLang: "English",
            devLanguages: ["Python", "Java", "JavaScript", "PHP", "SQL", "HTML5", "CSS3"],
            knowledge: {
                "Cyber Security": "Udemy.com Coursework",
                "Networking": "Udemy.com Coursework",
                "Object Oriented Programming": "50%"
            },
            fullName(){
                let fullName = this.fName + " " + this.lName;
                return fullName;
            },
            returnLangs(){
                let returnValue = "";
                this.devLanguages.forEach(element => {
                    returnValue += ("<li>" + element + "</li>");
                    return returnValue;
                })
                return returnValue;
            },
            returnKnowledge(){
                let returnValue = "";
                for (let [topic, value] of Object.entries(this.knowledge)){
                    returnValue += "<li>" + topic + ": " + value + "</li>";
                }
                return returnValue;
            }
        }
    return prog_developer;
    }
