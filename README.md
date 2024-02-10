pineApple Task Manager Project

project deployed on: https://pineapple-okxi.onrender.com
Please, do not judge the design, since the most work was put into website logic

This project represents a simple task management tool for a company (since there are a lot of brand in the world, I assume that "pineApple" was not taken yet xD).

This project covers all the stuff that was learned during the 5th modelu of the course I am attended to - Frameworks.

Thus, I have created a website which allows to create, assign and mark tasks as completed. Just imagine a company, in front of which there is a CEO. This CEO is a superuser of the website. His page is created once the project is deployed. The reason why the CEO is the superuser - he should always keep track of everything that happens in the company, inclusively defining their employees roles. So, if you would like to access the CEO's page:

login: m.gordilov
pass: P@ssw0rd1753!

After, there are employees. When they create a page, nothing specific happens, they are just empty pages. Once their profile is created, they are redirected to their profile page and they will need to update their profile. The reason for that is that they will have time to prepare their own profile photo and while changing the photo to change their department.

Now after introducing the department which users should choose manually when updating their profile, I would like to speak more about the task logic. So, when a task is created, it is possible to choose the department this task is designated to and who manages the respective task. Please, bear in mind that the status "manager" can only be given by the superuser (CEO) in the admin panel, in order for "funny employees" not to tick this box "just to check what happens". So, returning back to the task assigning logic, only the user from the same department as the task's department can take this task. E.g.: If a user from the risk department tries to take the task for Financial department, they will not be able to do that. Once the project is taken by the user, his card appears in the task details under the section displaying who works on the project.

The task can only be marked as completed only by the user who works on the task, person who manages the task or superuser (CEO). Please keep in mind that once task is comleted it is not possible to return it (except asking the CEO to do that, because all the work should be done responsibly!!!). Once someone completes a task, it goes to the "Completed tasks" section and its page still can be accessed. Completed tasks will also appear on the user's page under its profile details.

So I think that's everything about the project. Please, do not hesitate to play around it by creating different users and changing their departments/statuses/etc.

As mentioned previously, I tried to cover the maximum of Django functionality and think that this is achieved.

If there are any questions or queries, do not hesitate to contact me over the email: gordilovmaxim@gmail.com.