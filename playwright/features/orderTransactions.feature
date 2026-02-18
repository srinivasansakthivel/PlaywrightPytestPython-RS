Feature: Order Transaction
    Tests related to the order transaction process.

  Scenario Outline: Verify order success message shown in the details page
      Given place the item with <username> and <password>
      And the user is on the landing page

      When I login to portal with <username> and <password>
      And navigate to the order page
      And select the orderId

      Then order message is successfully displayed
      Examples:
          | username              | password    |
          | starsrini5@gmail.com  | Qwerty#1234 |