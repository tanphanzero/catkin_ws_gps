// Auto-generated. Do not edit!

// (in-package my_message.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Start_and_Goal {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.robot_x = null;
      this.robot_y = null;
      this.clicked_x = null;
      this.clicked_y = null;
    }
    else {
      if (initObj.hasOwnProperty('robot_x')) {
        this.robot_x = initObj.robot_x
      }
      else {
        this.robot_x = 0.0;
      }
      if (initObj.hasOwnProperty('robot_y')) {
        this.robot_y = initObj.robot_y
      }
      else {
        this.robot_y = 0.0;
      }
      if (initObj.hasOwnProperty('clicked_x')) {
        this.clicked_x = initObj.clicked_x
      }
      else {
        this.clicked_x = 0.0;
      }
      if (initObj.hasOwnProperty('clicked_y')) {
        this.clicked_y = initObj.clicked_y
      }
      else {
        this.clicked_y = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Start_and_Goal
    // Serialize message field [robot_x]
    bufferOffset = _serializer.float64(obj.robot_x, buffer, bufferOffset);
    // Serialize message field [robot_y]
    bufferOffset = _serializer.float64(obj.robot_y, buffer, bufferOffset);
    // Serialize message field [clicked_x]
    bufferOffset = _serializer.float64(obj.clicked_x, buffer, bufferOffset);
    // Serialize message field [clicked_y]
    bufferOffset = _serializer.float64(obj.clicked_y, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Start_and_Goal
    let len;
    let data = new Start_and_Goal(null);
    // Deserialize message field [robot_x]
    data.robot_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [robot_y]
    data.robot_y = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [clicked_x]
    data.clicked_x = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [clicked_y]
    data.clicked_y = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 32;
  }

  static datatype() {
    // Returns string type for a message object
    return 'my_message/Start_and_Goal';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'abd8c4caffbcef7e1dc7782b0e0d4428';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 robot_x
    float64 robot_y
    float64 clicked_x
    float64 clicked_y
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Start_and_Goal(null);
    if (msg.robot_x !== undefined) {
      resolved.robot_x = msg.robot_x;
    }
    else {
      resolved.robot_x = 0.0
    }

    if (msg.robot_y !== undefined) {
      resolved.robot_y = msg.robot_y;
    }
    else {
      resolved.robot_y = 0.0
    }

    if (msg.clicked_x !== undefined) {
      resolved.clicked_x = msg.clicked_x;
    }
    else {
      resolved.clicked_x = 0.0
    }

    if (msg.clicked_y !== undefined) {
      resolved.clicked_y = msg.clicked_y;
    }
    else {
      resolved.clicked_y = 0.0
    }

    return resolved;
    }
};

module.exports = Start_and_Goal;
