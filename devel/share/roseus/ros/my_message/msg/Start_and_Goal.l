;; Auto-generated. Do not edit!


(when (boundp 'my_message::Start_and_Goal)
  (if (not (find-package "MY_MESSAGE"))
    (make-package "MY_MESSAGE"))
  (shadow 'Start_and_Goal (find-package "MY_MESSAGE")))
(unless (find-package "MY_MESSAGE::START_AND_GOAL")
  (make-package "MY_MESSAGE::START_AND_GOAL"))

(in-package "ROS")
;;//! \htmlinclude Start_and_Goal.msg.html


(defclass my_message::Start_and_Goal
  :super ros::object
  :slots (_robot_x _robot_y _clicked_x _clicked_y ))

(defmethod my_message::Start_and_Goal
  (:init
   (&key
    ((:robot_x __robot_x) 0.0)
    ((:robot_y __robot_y) 0.0)
    ((:clicked_x __clicked_x) 0.0)
    ((:clicked_y __clicked_y) 0.0)
    )
   (send-super :init)
   (setq _robot_x (float __robot_x))
   (setq _robot_y (float __robot_y))
   (setq _clicked_x (float __clicked_x))
   (setq _clicked_y (float __clicked_y))
   self)
  (:robot_x
   (&optional __robot_x)
   (if __robot_x (setq _robot_x __robot_x)) _robot_x)
  (:robot_y
   (&optional __robot_y)
   (if __robot_y (setq _robot_y __robot_y)) _robot_y)
  (:clicked_x
   (&optional __clicked_x)
   (if __clicked_x (setq _clicked_x __clicked_x)) _clicked_x)
  (:clicked_y
   (&optional __clicked_y)
   (if __clicked_y (setq _clicked_y __clicked_y)) _clicked_y)
  (:serialization-length
   ()
   (+
    ;; float64 _robot_x
    8
    ;; float64 _robot_y
    8
    ;; float64 _clicked_x
    8
    ;; float64 _clicked_y
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _robot_x
       (sys::poke _robot_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _robot_y
       (sys::poke _robot_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _clicked_x
       (sys::poke _clicked_x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _clicked_y
       (sys::poke _clicked_y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _robot_x
     (setq _robot_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _robot_y
     (setq _robot_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _clicked_x
     (setq _clicked_x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _clicked_y
     (setq _clicked_y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get my_message::Start_and_Goal :md5sum-) "abd8c4caffbcef7e1dc7782b0e0d4428")
(setf (get my_message::Start_and_Goal :datatype-) "my_message/Start_and_Goal")
(setf (get my_message::Start_and_Goal :definition-)
      "float64 robot_x
float64 robot_y
float64 clicked_x
float64 clicked_y

")



(provide :my_message/Start_and_Goal "abd8c4caffbcef7e1dc7782b0e0d4428")


