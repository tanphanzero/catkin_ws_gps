
(cl:in-package :asdf)

(defsystem "my_message-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Start_and_Goal" :depends-on ("_package_Start_and_Goal"))
    (:file "_package_Start_and_Goal" :depends-on ("_package"))
  ))