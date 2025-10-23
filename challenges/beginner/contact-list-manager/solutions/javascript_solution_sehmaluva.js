const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let contacts = [];

function addContact() {
  rl.question('Enter name: ', (name) => {
    rl.question('Enter phone number: ', (phone) => {
      contacts.push({ name, phone });
      console.log(`Contact '${name}' added.`);
      mainMenu();
    });
  });
}

function viewContacts() {
  console.log('\n--- Your Contacts ---');
  if (contacts.length === 0) {
    console.log('Your contact list is empty.');
  } else {
    contacts.forEach((contact, index) => {
      console.log(`${index + 1}. ${contact.name} - ${contact.phone}`);
    });
  }
  console.log('---------------------\n');
  mainMenu();
}

function deleteContact() {
  rl.question('Enter name to delete: ', (name) => {
    const initialLength = contacts.length;
    contacts = contacts.filter(contact => contact.name.toLowerCase() !== name.toLowerCase());
    if (contacts.length < initialLength) {
      console.log(`Contact '${name}' deleted.`);
    } else {
      console.log(`Contact '${name}' not found.`);
    }
    mainMenu();
  });
}

function mainMenu() {
  rl.question('Enter a command (add, view, delete, exit): ', (command) => {
    switch (command.toLowerCase()) {
      case 'add':
        addContact();
        break;
      case 'view':
        viewContacts();
        break;
      case 'delete':
        deleteContact();
        break;
      case 'exit':
        console.log('Goodbye!');
        rl.close();
        break;
      default:
        console.log('Invalid command.');
        mainMenu();
        break;
    }
  });
}

console.log('--- Contact List Manager ---');
mainMenu();
