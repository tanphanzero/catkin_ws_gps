; Auto-generated. Do not edit!


(cl:in-package mini_map_node-msg)


;//! \htmlinclude Start_and_Goal.msg.html

(cl:defclass <Start_and_Goal> (roslisp-msg-protocol:ros-message)
  ((robot_x
    :reader robot_x
    :initarg :robot_x
    :type cl:float
    :initform 0.0)
   (robot_y
    :reader robot_y
    :initarg :robot_y
    :type cl:float
    :initform 0.0)
   (clicked_x
    :reader clicked_x
    :initarg :clicked_x
    :type cl:float
    :initform 0.0)
   (clicked_y
    :reader clicked_y
    :initarg :clicked_y
    :type cl:float
    :initform 0.0))
)

(cl:defclass Start_and_Goal (<Start_and_Goal>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Start_and_Goal>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Start_and_Goal)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name mini_map_node-msg:<Start_and_Goal> is deprecated: use mini_map_node-msg:Start_and_Goal instead.")))

(cl:ensure-generic-function 'robot_x-val :lambda-list '(m))
(cl:defmethod robot_x-val ((m <Start_and_Goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini_map_node-msg:robot_x-val is deprecated.  Use mini_map_node-msg:robot_x instead.")
  (robot_x m))

(cl:ensure-generic-function 'robot_y-val :lambda-list '(m))
(cl:defmethod robot_y-val ((m <Start_and_Goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini_map_node-msg:robot_y-val is deprecated.  Use mini_map_node-msg:robot_y instead.")
  (robot_y m))

(cl:ensure-generic-function 'clicked_x-val :lambda-list '(m))
(cl:defmethod clicked_x-val ((m <Start_and_Goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini_map_node-msg:clicked_x-val is deprecated.  Use mini_map_node-msg:clicked_x instead.")
  (clicked_x m))

(cl:ensure-generic-function 'clicked_y-val :lambda-list '(m))
(cl:defmethod clicked_y-val ((m <Start_and_Goal>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader mini_map_node-msg:clicked_y-val is deprecated.  Use mini_map_node-msg:clicked_y instead.")
  (clicked_y m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Start_and_Goal>) ostream)
  "Serializes a message object of type '<Start_and_Goal>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'robot_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'robot_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'clicked_x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'clicked_y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Start_and_Goal>) istream)
  "Deserializes a message object of type '<Start_and_Goal>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'robot_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'robot_y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'clicked_x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'clicked_y) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Start_and_Goal>)))
  "Returns string type for a message object of type '<Start_and_Goal>"
  "mini_map_node/Start_and_Goal")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Start_and_Goal)))
  "Returns string type for a message object of type 'Start_and_Goal"
  "mini_map_node/Start_and_Goal")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Start_and_Goal>)))
  "Returns md5sum for a message object of type '<Start_and_Goal>"
  "abd8c4caffbcef7e1dc7782b0e0d4428")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Start_and_Goal)))
  "Returns md5sum for a message object of type 'Start_and_Goal"
  "abd8c4caffbcef7e1dc7782b0e0d4428")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Start_and_Goal>)))
  "Returns full string definition for message of type '<Start_and_Goal>"
  (cl:format cl:nil "float64 robot_x~%float64 robot_y~%float64 clicked_x~%float64 clicked_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Start_and_Goal)))
  "Returns full string definition for message of type 'Start_and_Goal"
  (cl:format cl:nil "float64 robot_x~%float64 robot_y~%float64 clicked_x~%float64 clicked_y~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Start_and_Goal>))
  (cl:+ 0
     8
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Start_and_Goal>))
  "Converts a ROS message object to a list"
  (cl:list 'Start_and_Goal
    (cl:cons ':robot_x (robot_x msg))
    (cl:cons ':robot_y (robot_y msg))
    (cl:cons ':clicked_x (clicked_x msg))
    (cl:cons ':clicked_y (clicked_y msg))
))
